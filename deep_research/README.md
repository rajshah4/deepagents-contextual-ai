# Deep Research Agent Example

A standalone example demonstrating how to build a research agent using the `deepagents` package with custom tools for web search and strategic thinking.

## Overview

This example shows how to create a "deep agent" - an AI agent that can:
- Break down complex research tasks into manageable steps
- Use a virtual file system to store and retrieve information
- Spawn subagents to parallelize research
- Perform web searches with context offloading
- Reflect strategically on research progress

The key insight: **you only need to provide domain-specific tools** (like web search) while the `deepagents` package gives you all the "deep agent" infrastructure (planning, file system, subagents, context management) automatically.

## Architecture

### Built-in Tools (Free with `deepagents`)

When you call `create_deep_agent()`, you automatically get **9+ built-in tools**:

**1. TODO Management** (1 tool)
- `write_todos` - Planning and task decomposition

**2. File System** (7 tools)
- `ls` - List files in a directory
- `read_file` - Read file contents with pagination support
- `write_file` - Create new files
- `edit_file` - Edit existing files with string replacement
- `glob` - Find files matching patterns (e.g., `**/*.py`)
- `grep` - Search for text within files
- `execute` - Run shell commands (if sandbox backend provided)

**3. Subagent Spawning** (1 tool)
- `task` - Delegate complex subtasks to specialized subagents with isolated context

### Custom Tools (Added by You)

This example provides **2 custom research tools**:

**1. `tavily_search` - Web Search with Context Offloading**
- Performs web searches using Tavily API
- Fetches full webpage content via HTTP
- Converts HTML to markdown using `markdownify`
- Saves full content to files (context offloading)
- Returns only minimal summaries to avoid context spam
- Uses LangGraph `Command` to update both files and messages

**2. `think_tool` - Strategic Reflection**
- Provides structured reflection mechanism
- Helps agent pause and assess progress between searches
- Analyzes findings, identifies gaps, and plans next steps

### Custom Prompts

The example includes specialized prompts for research workflows:
- `RESEARCHER_INSTRUCTIONS` - Instructions for the research subagent
- `TODO_USAGE_INSTRUCTIONS` - Guidelines for planning and task decomposition
- `FILE_USAGE_INSTRUCTIONS` - How to use the virtual file system
- `SUBAGENT_INSTRUCTIONS` - When and how to delegate to subagents

## Installation

### Prerequisites

- Python 3.11+
- UV or pip for package management
- API keys for:
  - Anthropic (for Claude)
  - OpenAI (for GPT-4o-mini summarization)
  - Tavily (for web search)

### Setup

1. **Clone and navigate to this directory:**
   ```bash
   cd examples/deep_research/
   ```

2. **Create a virtual environment with UV:**
   ```bash
   uv venv
   ```

   This creates a `.venv` directory with an isolated Python environment.

3. **Activate the virtual environment:**

   On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

   On Windows:
   ```bash
   .venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   uv pip install -e .
   ```

   Or with pip (if not using UV):
   ```bash
   pip install -e .
   ```

5. **Set up environment variables:**

   Copy the example env file and fill in your API keys:
   ```bash
   cp .env.example .env
   ```

   Then edit `.env` to add your actual API keys:
   ```bash
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

## Usage

### Option 1: Python Script

Run research from the command line:

```bash
python run_research.py "Your research question here"
```

**Example:**
```bash
python run_research.py "Give me a brief overview of Model Context Protocol (MCP)"
```

The script will:
1. Initialize the deep research agent
2. Execute the research workflow
3. Display the message history with results

### Option 2: Jupyter Notebook

Open and run `research_agent.ipynb` for an interactive experience:

```bash
jupyter notebook research_agent.ipynb
```

**Important**: Make sure to select the correct kernel in Jupyter:
- Click "Kernel" → "Change Kernel" → Select the kernel corresponding to your `.venv` environment
- Or if you installed with UV in the parent workspace, select that Python environment

The notebook provides:
- Step-by-step walkthrough of the architecture
- Visual graph of the agent structure
- Interactive cells to run research queries
- Rich formatted output

### Option 3: LangGraph Deployment

Deploy the agent using LangGraph Studio or LangGraph Cloud:

**Local Development with LangGraph Studio:**
1. Open LangGraph Studio
2. Select the `deep_research` directory
3. The agent will be loaded from `agent.py` as configured in `langgraph.json`
4. Interact with the agent through the Studio interface

**LangGraph Cloud Deployment:**
```bash
# Deploy to LangGraph Cloud
langgraph deploy
```

The `langgraph.json` configuration:
- **Graph name**: `research`
- **Entry point**: `./agent.py:agent`
- **Dependencies**: Current directory (`.`)
- **Environment**: Variables loaded from `.env`

## Key Concepts

### 1. File-Based Report Generation

The agent writes structured reports to `/final_report.md` with professional formatting:

- **Structured approach**: Different patterns for comparisons, lists, summaries
- **Numbered citations**: Inline references [1], [2] with Sources section
- **Professional style**: Text-heavy paragraphs, no self-referential language
- **Verification**: Saves original question to `/research_request.md` for validation

This creates a clear separation between the research process and the final deliverable.

### 2. Context Offloading

The `tavily_search` tool demonstrates a critical pattern for long-running agent trajectories:

- **Problem**: Full search results consume too much context
- **Solution**: Save full content to files, return only summaries
- **Benefit**: Agent maintains focused context while retaining access to details

This pattern is inspired by [Manus's context engineering approach](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus).

### 3. Strategic Thinking

The `think_tool` creates deliberate pauses in the research workflow:

```python
@tool(parse_docstring=True)
def think_tool(reflection: str) -> str:
    """Tool for strategic reflection on research progress."""
    return f"Reflection recorded: {reflection}"
```

This simple tool encourages the agent to:
- Analyze findings after each search
- Assess information gaps
- Decide whether to continue searching or provide an answer

### 4. Parallel Research

The subagent system enables parallel research execution:

```python
research_sub_agent = {
    "name": "research-agent",
    "description": "Delegate research to the sub-agent researcher.",
    "prompt": RESEARCHER_INSTRUCTIONS,
    "tools": ["tavily_search", "think_tool"],
}
```

The main agent can spawn multiple research subagents in parallel:
- **Simple queries**: 1 subagent
- **Comparisons**: 1 subagent per element (e.g., "Compare X vs Y vs Z" → 3 subagents)
- **Multi-faceted research**: 1 subagent per aspect

### 5. Built-in Context Management

The `deepagents` package automatically includes:
- **SummarizationMiddleware** - Compresses context when it gets too long
- **AnthropicPromptCachingMiddleware** - Optimizes prompt caching
- **HumanInTheLoopMiddleware** - Optional approval workflows

## Project Structure

```
deep_research/
├── README.md                    # This file
├── pyproject.toml              # Project dependencies
├── langgraph.json              # LangGraph deployment configuration
├── agent.py                    # Standalone agent for LangGraph (exports 'agent')
├── run_research.py             # Standalone Python script for testing
├── research_agent.ipynb        # Interactive Jupyter notebook
├── utils.py                    # Display utilities (Rich formatting)
└── research_agent/             # Research agent module
    ├── __init__.py            # Module exports
    ├── tools.py               # Custom tools (tavily_search, think_tool)
    └── prompts.py             # Custom prompts and instructions
```

## Example Output

When you run a research query, the agent will:

1. **Save the research question** to `/research_request.md`
2. **Plan the research** using `write_todos`
3. **Delegate to subagent(s)** using `task`
4. **Execute searches** using `tavily_search`
5. **Reflect on findings** using `think_tool`
6. **Write final report** to `/final_report.md` with numbered citations
7. **Verify completeness** by reading `/research_request.md`

The output includes:
- Search summaries with file references
- Strategic reflections at each step
- Professional report in `/final_report.md` with:
  - Structured sections (comparisons, lists, or summaries)
  - Numbered inline citations [1], [2], [3]
  - Sources section with full URLs
  - Comprehensive, text-heavy content

## Customization

### Adding New Tools

To add your own domain-specific tools:

1. Define a tool in `research_agent/tools.py`:
   ```python
   @tool(parse_docstring=True)
   def your_custom_tool(param: str) -> str:
       """Your tool description."""
       # Your implementation
       return result
   ```

2. Add it to the tools list:
   ```python
   sub_agent_tools = [tavily_search, think_tool, your_custom_tool]
   ```

3. Update the subagent configuration:
   ```python
   research_sub_agent = {
       "tools": ["tavily_search", "think_tool", "your_custom_tool"],
   }
   ```

### Modifying Prompts

Customize the research behavior by editing prompts in `research_agent/prompts.py`:

- `RESEARCHER_INSTRUCTIONS` - Change research strategy
- `TODO_USAGE_INSTRUCTIONS` - Adjust planning behavior
- `SUBAGENT_INSTRUCTIONS` - Modify delegation logic

## Dependencies

Key packages used in this example:

- **deepagents** - Core deep agent framework
- **langgraph** - LangChain's graph-based agent framework
- **langchain** - LLM abstraction and utilities
- **tavily-python** - Web search API
- **httpx** - HTTP client for fetching webpages
- **markdownify** - HTML to Markdown conversion
- **rich** - Beautiful terminal output
- **pydantic** - Data validation
- **jupyter** - Interactive notebooks

See `pyproject.toml` for complete dependency list.

## Learn More

- [DeepAgents Documentation](../../README.md) - Main package documentation
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/) - Graph-based agent framework
- [Manus Context Engineering](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) - Inspiration for context offloading pattern

## License

This example is part of the deepagents project. See the main repository for license information.
