"""Research Tools.

This module provides search and content processing utilities for the research agent,
using Tavily for URL discovery and fetching full webpage content, and ContextualAI
for RAG-based document search.
"""

import os
import httpx
from langchain_core.tools import InjectedToolArg, tool
from markdownify import markdownify
from tavily import TavilyClient
from typing_extensions import Annotated, Literal

try:
    from contextual import ContextualAI
    CONTEXTUAL_AI_AVAILABLE = True
except ImportError:
    CONTEXTUAL_AI_AVAILABLE = False

tavily_client = TavilyClient()

# Initialize ContextualAI client if available
contextual_client = None
contextual_agent_id = None
if CONTEXTUAL_AI_AVAILABLE:
    api_key = os.getenv("CONTEXTUAL_AI_API_KEY")
    contextual_agent_id = os.getenv("CONTEXTUAL_AI_AGENT_ID")
    if api_key:
        contextual_client = ContextualAI(api_key=api_key)


def fetch_webpage_content(url: str, timeout: float = 10.0) -> str:
    """Fetch and convert webpage content to markdown.

    Args:
        url: URL to fetch
        timeout: Request timeout in seconds

    Returns:
        Webpage content as markdown
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = httpx.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return markdownify(response.text)
    except Exception as e:
        return f"Error fetching content from {url}: {str(e)}"


@tool(parse_docstring=True)
def tavily_search(
    query: str,
    max_results: Annotated[int, InjectedToolArg] = 1,
    topic: Annotated[
        Literal["general", "news", "finance"], InjectedToolArg
    ] = "general",
) -> str:
    """Search the web for information on a given query.

    Uses Tavily to discover relevant URLs, then fetches and returns full webpage content as markdown.

    Args:
        query: Search query to execute
        max_results: Maximum number of results to return (default: 1)
        topic: Topic filter - 'general', 'news', or 'finance' (default: 'general')

    Returns:
        Formatted search results with full webpage content
    """
    # Use Tavily to discover URLs
    search_results = tavily_client.search(
        query,
        max_results=max_results,
        topic=topic,
    )

    # Fetch full content for each URL
    result_texts = []
    for result in search_results.get("results", []):
        url = result["url"]
        title = result["title"]

        # Fetch webpage content
        content = fetch_webpage_content(url)

        result_text = f"""## {title}
**URL:** {url}

{content}

---
"""
        result_texts.append(result_text)

    # Format final response
    response = f"""🔍 Found {len(result_texts)} result(s) for '{query}':

{chr(10).join(result_texts)}"""

    return response


@tool(parse_docstring=True)
def contextual_search(
    query: str,
    max_results: Annotated[int, InjectedToolArg] = 10,
) -> str:
    """Search ContextualAI RAG knowledge base for information on a given query.

    Uses ContextualAI to retrieve relevant document chunks from the configured knowledge base.
    Returns formatted results with full content and attribution metadata.

    Args:
        query: Search query to execute
        max_results: Maximum number of results to return (default: 10)

    Returns:
        Formatted search results with document content and attribution
    """
    if not CONTEXTUAL_AI_AVAILABLE:
        return "Error: ContextualAI package is not installed. Please install it to use this tool."
    
    if not contextual_client or not contextual_agent_id:
        return "Error: ContextualAI client not configured. Please set CONTEXTUAL_AI_API_KEY and CONTEXTUAL_AI_AGENT_ID environment variables."

    try:
        # Query ContextualAI with include_retrieval_content_text to get actual content
        query_result = contextual_client.agents.query.create(
            agent_id=contextual_agent_id,
            messages=[{
                "content": query,
                "role": "user"
            }],
            retrievals_only=True,
            include_retrieval_content_text=True
        )

        # Extract retrieval contents
        retrieval_contents = query_result.retrieval_contents or []
        
        # Limit results
        retrieval_contents = retrieval_contents[:max_results]

        if not retrieval_contents:
            return f"🔍 No results found for '{query}' in ContextualAI knowledge base."

        # Format results
        result_texts = []
        for i, content in enumerate(retrieval_contents, 1):
            doc_name = getattr(content, 'doc_name', 'Unknown Document')
            content_text = getattr(content, 'content_text', None)
            content_id = getattr(content, 'content_id', 'N/A')
            doc_id = getattr(content, 'doc_id', 'N/A')
            page = getattr(content, 'page', None)
            format_type = getattr(content, 'format', 'unknown')
            score = getattr(content, 'score', None)

            # Build attribution string
            attribution_parts = [f"Context ID: {content_id}", f"Doc ID: {doc_id}"]
            if page is not None:
                attribution_parts.append(f"Page: {page}")
            attribution = " | ".join(attribution_parts)
            
            if score is not None:
                attribution += f" | Score: {score:.4f}"

            # Format content
            if content_text:
                content_display = content_text
            else:
                content_display = f"[Content not available - {format_type} format]"

            result_text = f"""## {doc_name}
**Attribution:** {attribution}

{content_display}

---
"""
            result_texts.append(result_text)

        # Format final response
        response = f"""🔍 Found {len(result_texts)} result(s) for '{query}' in ContextualAI knowledge base:

{chr(10).join(result_texts)}"""
        
        return response

    except Exception as e:
        return f"Error searching ContextualAI knowledge base: {str(e)}"


@tool(parse_docstring=True)
def think_tool(reflection: str) -> str:
    """Tool for strategic reflection on research progress and decision-making.

    Use this tool after each search to analyze results and plan next steps systematically.
    This creates a deliberate pause in the research workflow for quality decision-making.

    When to use:
    - After receiving search results: What key information did I find?
    - Before deciding next steps: Do I have enough to answer comprehensively?
    - When assessing research gaps: What specific information am I still missing?
    - Before concluding research: Can I provide a complete answer now?

    Reflection should address:
    1. Analysis of current findings - What concrete information have I gathered?
    2. Gap assessment - What crucial information is still missing?
    3. Quality evaluation - Do I have sufficient evidence/examples for a good answer?
    4. Strategic decision - Should I continue searching or provide my answer?

    Args:
        reflection: Your detailed reflection on research progress, findings, gaps, and next steps

    Returns:
        Confirmation that reflection was recorded for decision-making
    """
    return f"Reflection recorded: {reflection}"
