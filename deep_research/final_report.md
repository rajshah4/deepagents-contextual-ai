# NVIDIA's Three Biggest Bets: Fact vs. Reality Analysis

## Executive Summary

NVIDIA's three major strategic bets present dramatically different risk profiles. **Data Center** remains the crown jewel with 217% growth but faces mounting competitive threats from AMD and hyperscaler custom chips. **Automotive** is struggling with declining revenue and fierce competition, representing NVIDIA's most challenging market. **Sovereign AI** shows promise but remains largely aspirational, with most deals being multi-year commitments rather than current deployments. The gap between NVIDIA's confident public narrative and market reality is widest in Automotive, moderate in Sovereign AI, and narrowest (but growing) in Data Center.

---

## 1. AUTOMOTIVE: The Struggling Bet

### NVIDIA's Official Claims

NVIDIA positions automotive as one of four "large markets" with a **$14 billion design win pipeline over six years** (announced May 2023) [1]. The company claims to work with "several hundred partners in the automotive ecosystem" and offers an end-to-end solution through the NVIDIA DRIVE platform, including DRIVE Hyperion hardware, sensors, and software for autonomous driving and AI cockpit applications [2].

**Key Products**: DRIVE AGX computing hardware, DRIVE Chauffeur (autonomous driving), DRIVE Concierge (in-vehicle experiences), and DRIVE Sim for testing and validation [2].

**Stated Partnerships**: BYD, XPENG, MediaTek, Foxconn, Mercedes-Benz, and Jaguar Land Rover [3][4][5].

**Revenue Performance (Official)**:
- FY2023: +60% year-over-year growth [6]
- Q1 FY2024: $296M (+114% YoY) [3]
- Q2 FY2024: $253M (+15% YoY, -15% sequential) [4]
- Q3 FY2024: $261M (+4% YoY) [5]

**Critical Caveat**: NVIDIA repeatedly warns in SEC filings that "achieving design wins does not guarantee revenue" and investments "may not produce meaningful revenue for several years, if at all" [7].

### Market Reality: Decline and Fierce Competition

**Revenue Reality**:
- **Q4 FY2024: $281M, DOWN 4% year-over-year** [8]
- Full FY2024 automotive revenue: approximately $1 billion
- This represents a tiny fraction compared to NVIDIA's $18.4 billion data center revenue in Q4 alone [8]

**The Competitive Landscape**:

**Qualcomm is Winning**: Automotive revenue of $598M, **UP 31% year-over-year**—growing more than twice as fast as NVIDIA's total automotive business [8]. Industry analyst Steve McDowell notes: "Qualcomm has an intrinsic advantage over Nvidia in this market, as Qualcomm has long led the way in providing connectivity solutions to the automotive industry" [8].

**Power Efficiency Advantage**: Qualcomm's inference accelerators "excel at delivering AI inference, outperforming Nvidia in power efficiency—a critical capability in an automobile" [8].

**Tesla's In-House Threat**: Tesla has developed its own Full Self-Driving (FSD) chip, completely bypassing NVIDIA's solutions [9]. This validates the viability of in-house chip development for large automakers—a risk NVIDIA explicitly acknowledges in its 10-K filings [10].

**Chinese Competition**: Huawei's MDC 600 chip is identified as "a strong competitor with high performance and cost efficiency" [9]. Other Chinese competitors include Horizon Robotics, Black Sesame Technologies, and Xin Chi Technology. While NVIDIA holds approximately 33.5% market share in China (driven by NIO, XPeng, and Li Auto), this position faces increasing pressure from domestic alternatives backed by China's localization efforts [9].

**Intel and AMD**: Both announced new automotive-targeted SoCs at CES 2024, providing compelling alternatives for subsystem suppliers [8].

### Partnership Reality Check

**Mercedes-Benz**: The flagship partnership announced in June 2020 promised deployment of NVIDIA DRIVE platform across Mercedes fleet "starting in 2024" with "the most sophisticated and advanced computing architecture ever deployed in an automobile" [11]. Despite the 2024 deployment timeline, **no recent news confirms actual production vehicle deployments in 2024**. The absence of follow-up announcements suggests either delays, limited rollout, or scaled-back ambitions.

**Jaguar Land Rover**: No recent updates found regarding NVIDIA partnerships, despite previous announcements.

### Analyst Assessment: "A Challenging Journey"

Forbes analyst Steve McDowell provided a sobering assessment in February 2024 [8]:

- "Nvidia doesn't have the dominance or lock-in it enjoys in the broader data center market"
- "This will continue to be a challenging journey for Nvidia"
- "It's been a long time since Nvidia faced a market as competitive as in-vehicle automotive"

**Critical Weakness**: "Advanced driving systems rely on AI inference, this isn't a market that requires data center class accelerators. It's also not a market that relies on Nvidia's CUDA software stack, offering a lower competitive barrier to entry" [8].

NVIDIA's CUDA moat—the foundation of its data center dominance—provides **no advantage in automotive**.

### Where NVIDIA Actually Succeeds

The analysis reveals NVIDIA's true automotive strength lies in the **data center side** of automotive AI, not in-vehicle compute [8]:
- Nearly 80 vehicle manufacturers use NVIDIA's AI infrastructure to train models
- NVIDIA contributed more than $1 billion to its data center business from automotive customers in FY2024
- **The disconnect**: "That success doesn't necessarily translate into in-vehicle design wins" [8]

### Structural Disadvantages

1. **No Connectivity Solutions**: Unlike Qualcomm, NVIDIA lacks integrated connectivity solutions (5G, V2X), requiring automakers to integrate multiple suppliers [8]
2. **Power Efficiency Concerns**: Automotive applications prioritize power efficiency over raw performance
3. **No Software Lock-In**: The automotive market doesn't rely on CUDA, eliminating software lock-in [8]
4. **Established Competitors**: Traditional suppliers (Bosch, Visteon, Continental) partner with multiple chip providers, preventing single-vendor dominance [8]

### Verdict: Cracks in the Narrative

**NVIDIA's $14 billion pipeline claim** stands in stark contrast to actual revenue performance. With quarterly revenues in the $250-450M range and Q4 FY2024 showing a 4% decline, the automotive sector represents NVIDIA's most challenging market entry in years. Analyst McDowell concludes: "Nvidia doesn't need to play in the automotive segment. While its AI data center business is unlikely to maintain its current growth rate and high margins over the long term, it will remain a significant market where Nvidia is the incumbent" [8].

The automotive bet shows **significant cracks**: declining revenue, competitors growing faster, major customers going in-house, unclear partnership deployments, and no competitive moat.

---

## 2. DATA CENTER: Dominance Under Siege

### NVIDIA's Official Claims

NVIDIA positions itself as a "full-stack computing infrastructure company with data-center-scale offerings" [12]. The company achieved explosive growth with **Data Center revenue of $47.5 billion in FY2024, up 217% from FY2023** [13], representing approximately 78% of total company revenue.

**Key Claims**:
- **Market Position**: 70-95% market share in AI accelerators [14]
- **CUDA Ecosystem**: 3.8 million developers worldwide using CUDA [15]
- **Inference Leadership**: Approximately 40% of Data Center revenue (~$19 billion) from AI inference in FY2024 [13]
- **Cloud Dominance**: Large cloud providers represented more than half of Data Center revenue in Q4 FY2024 [13]
- **Supercomputing Leadership**: NVIDIA powers over 75% of supercomputers on the global TOP500 list [13]

**Product Portfolio**: H100, H200, GH200 Grace Hopper Superchip, L40S, L4 Tensor Core GPU, Spectrum-X networking, and upcoming Blackwell architecture [16][17][18].

**Acknowledged Risks**: NVIDIA explicitly names competitors including AMD, Intel, Huawei, and critically, "large cloud services companies with internal teams designing hardware and software" such as Alibaba, Alphabet, Amazon, Baidu, and Microsoft [19]. The company warns: "Some of our customers have in-house expertise and internal development capabilities similar to some of ours and can use or develop their own solutions to replace those we are providing" [20].

**Customer Concentration**: One data center distributor represents ~17% of total revenue, and one large cloud service provider (indirect) represents ~22% of total revenue [21].

### Market Reality: Mounting Competitive Threats

**DOJ Antitrust Investigation**: In October 2024, the Department of Justice initiated a formal antitrust investigation into NVIDIA, issuing subpoenas to examine potential anticompetitive practices [14]. Key concerns include:
- Illegal tying agreements bundling AI chips with software and services
- Customer prioritization favoring those who can immediately deploy products
- Bundling practices making it difficult for customers to choose alternative vendors

The investigation reflects growing concerns that NVIDIA's market dominance has crossed into potentially anticompetitive territory.

**AMD's Competitive Breakthrough**: AMD's MI300X AI accelerator is gaining significant traction with major hyperscalers [22]:
- **Meta**: 173,000+ MI300X chips deployed
- **Microsoft Azure**: MI300X instances now available
- **Oracle Cloud Infrastructure**: Launched OCI Supercluster with AMD MI300X supporting up to 16,384 GPUs in a single cluster (September 2024)
- **Vultr**: Cloud computing platform adopted MI300X

AMD CEO Lisa Su stated: "We launched MI300X in December. It has had just tremendous customer traction and customers have been really excited about it" [22]. AMD's roadmap includes MI325 (Q4 2024), MI350 series (2025), and MI400 (future generation), with heavy investment in ROCm software to compete with CUDA [22].

**Hyperscaler Custom Chip Initiatives: The Existential Threat**

Major cloud providers are developing custom AI ASICs specifically to "reduce their reliance on NVIDIA and optimize for specific workloads" [23]. This represents a fundamental shift in market structure.

**Google TPU**: The most advanced program with approximately **$8 billion per year investment with Broadcom alone** [23]. TPUs are "the cornerstone pillar to Google's AI strategy," powering Google's Gemini model internally while being offered through Google Cloud Platform. Google has achieved "superior price-performance across successive TPU generations" [23].

**Microsoft Maia**: Maia 100 AI Accelerator designed on 3nm process by TSMC, developed in partnership with Marvell. Microsoft is "integrating custom silicon to boost performance and reduce reliance on external hardware sources" while improving data center energy efficiency [23].

**Amazon Trainium and Inferentia**: Optimized for training and inference workloads respectively. However, Amazon "continues to face challenges transitioning AI workloads from NVIDIA's CUDA platform, necessitating significant software development and ecosystem support" [23]. AWS appears "behind Google TPUs and Microsoft in its custom AI ASICs" [23].

**Meta MTIA**: Meta runs **over 2 trillion inference operations per day**—more than any other company globally—across content recommendation, advertising targeting, and user behavior prediction [23]. CEO Mark Zuckerberg announced **over $20 billion of investment in GPUs and AI data center infrastructure** [23]. MTIA processors are developed using Broadcom's 7nm, 5nm, and 3nm technologies.

**The ARM CPU Precedent**: The Big 3 cloud providers collectively utilize an estimated 50.4 million CPUs in their infrastructure, predominantly ARM-based processors chosen over Intel/AMD for cost efficiency [23]. Typical Intel CPU costs ~$1,000 vs. ARM CPU ~$600, resulting in **total savings of over $20 billion** for the Big 3 clouds [23]. This precedent demonstrates that hyperscalers can successfully develop custom silicon at scale, achieving "40%+ better price performance" than traditional vendors [23].

### Customer Diversification: Both Sides Hedging

**NVIDIA's Counter-Strategy**: Recognizing the threat from hyperscaler custom chips, NVIDIA is actively diversifying its customer base beyond traditional Big Tech companies [24]:
- **Nation-states**: Multi-billion-dollar agreement with Saudi Arabia for AI infrastructure
- **"Neoclouds"**: Next-generation cloud service providers like CoreWeave and Lambda
- **Regional cloud providers**: Expanding into markets outside traditional hyperscaler dominance

This diversification aims to "reduce dependency on traditional tech giants" who are developing competing custom silicon [24].

**Hyperscaler Multi-Sourcing**: Major cloud providers are pursuing multi-vendor strategies:
- Microsoft Azure offers both NVIDIA GPUs and AMD MI300X instances
- Oracle Cloud deployed AMD MI300X at massive scale (16,384 GPU clusters)
- Meta is deploying 173,000+ AMD MI300X chips alongside NVIDIA GPUs

This represents a fundamental shift from NVIDIA exclusivity to portfolio diversification.

### Supply, Demand, and Pricing Dynamics

In September 2024, NVIDIA publicly refuted media reports about supply constraints, stating: "We have more than enough H100/H200 to satisfy every order without delay" [25]. However, market reality shows:
- **Zero chip sales to China in Q2 2025** due to export restrictions [25]
- **Data center revenue miss**: $41.1B actual vs. $41.3B expected in Q2 2025 [25]
- **Margin compression**: Operating margins declined from 66.4% to 64.5% year-over-year [25]

These indicators suggest potential demand normalization or competitive pressure, though NVIDIA maintains strong overall growth (56% YoY revenue growth) [25].

### Export Control Impact

**China Market Decline**: China represented 19% of Data Center revenue in FY2023, dropped to 14% in FY2024, and by Q4 FY2024 was "mid-single digit percentage" of Data Center revenue [26]. In October 2023, the US government announced new licensing requirements for exports to China and other countries (including Saudi Arabia, UAE, Vietnam) for products exceeding certain performance thresholds, including A100, A800, H100, H800, L4, L40, L40S, and RTX 4090 [26].

**Critical Statement**: "We have not received licenses to ship these restricted products to China" [26]. NVIDIA acknowledges: "Our competitive position has been harmed, and our competitive position and future results may be further harmed in the long term, if there are further changes in the USG's export controls" [26].

### Analyst Assessment

Analysts maintain a "Strong Buy" rating with a mean target price of $210.49 (23.3% upside potential as of September 2024) [25]:
- 38 analysts: Strong Buy
- 2 analysts: Moderate Buy
- 5 analysts: Hold
- 1 analyst: Strong Sell

**Key Concerns**: "The expectations around Nvidia have skyrocketed in recent years" making any miss trigger significant selloffs [25]. Recognition that hyperscaler custom chips represent long-term structural threat, and DOJ investigation could limit business practices.

### Verdict: Dominance Validated, But Threats Materializing

NVIDIA's data center dominance is **real and current**, with 217% revenue growth and 70-95% market share validating their official claims. However, the market reality reveals **unprecedented competitive and regulatory challenges**:

**Immediate Threats (2024-2025)**:
- AMD MI300X gaining traction with multiple hyperscaler deployments
- DOJ antitrust investigation into business practices
- Customer diversification efforts underway

**Medium-Term Threats (2025-2027)**:
- Hyperscaler custom chips at scale (Google TPU, Microsoft Maia, Meta MTIA)
- Software ecosystem maturation reducing CUDA lock-in
- Margin pressure from competition

**Long-Term Structural Challenges**:
- Largest customers becoming direct competitors
- ARM CPU precedent proving $20B+ savings model for custom silicon
- Inference workload shift to custom ASICs (Meta's 2T daily operations)

The combination of AMD's MI300X traction, massive hyperscaler custom chip investments ($8B+/year from Google alone), proven ARM CPU precedent, and DOJ antitrust scrutiny represents a multi-front assault on NVIDIA's dominance. While financial performance remains strong (56% revenue growth), the structural threats are materializing faster than the company's public narrative suggests.

---

## 3. SOVEREIGN AI: Aspirational Opportunity

### NVIDIA's Official Claims

NVIDIA defines Sovereign AI as "a nation's domestic capability to produce artificial intelligence using its own infrastructure, data, workforce, and business networks. The goal is to protect and preserve local languages, values, culture, and history" [27].

**Jensen Huang's Vision**: At the World Government Summit 2024 in Dubai, NVIDIA's CEO stated: "Every country needs its own artificial infrastructure (AI) ecosystem to turbocharge economic potential while protecting its own culture. You cannot allow that to be done by other people" [28]. He introduced the concept of "AI factories" that "will become the bedrock of modern economies around the world" [28].

**Announced Partnerships**:
- **South Korea**: Over a quarter-million NVIDIA GPUs across sovereign clouds and AI factories [27]
- **Germany**: Deutsche Telekom Industrial AI Cloud, "world's first Industrial AI Cloud" launching early 2026, deploying "tens of thousands of NVIDIA GPUs" [27]
- **France**: Sovereign AI infrastructure for AI-native companies, researchers, and enterprises [27]
- **Italy**: Collaboration with government, supercomputing organizations, academia, and industry partners [27]
- **United Kingdom**: Building sovereign compute infrastructure, investing in research and skills [27]
- **UAE**: Stargate UAE project powered by NVIDIA Grace Blackwell GB300 systems [27]
- **Saudi Arabia**: Partnership with HUMAIN (AI subsidiary of Saudi Arabia's Public Investment Fund) to build "AI factories of the future" [27]
- **European Telecommunications**: Orange, Fastweb, Swisscom, Telefónica, and Telenor building AI infrastructure [27]

**Strategic Rationale**: NVIDIA positions sovereign AI as critical to "economic growth, national security, cultural preservation, and innovation" [27]. The company frames itself as the essential infrastructure provider, offering end-to-end solutions from hardware (GPUs) to software (NVIDIA AI Enterprise, NeMo, Morpheus) to services (training, partnerships).

**Revenue Context**: NVIDIA does not break out "Sovereign AI" as a separate revenue segment in SEC filings. Sovereign AI revenue is included within the Data Center segment, which achieved $47.5 billion in FY2024 [13]. The company explicitly states confidence that sovereign AI growth in other regions will "more than offset" China revenue declines [29].

### Market Reality: Announcements vs. Deployments

**Confirmed Operational Deployments**:
1. **Germany**: Deutsche Telekom industrial AI cloud with 10,000 NVIDIA Blackwell GPUs—described as "world's first industrial AI cloud" and OPERATIONAL [30]
2. **France**: 18,000 NVIDIA Grace Blackwell systems with Mistral AI—announced June 2025, deployment in progress with expansion planned across multiple locations in 2026 [30]
3. **European DGX Cloud**: Expansion operational [30]

**Announced But Not Yet Deployed**:
1. **Saudi Arabia HUMAIN**: Up to 500 megawatts capacity with "several hundred thousand" GPUs over 5 years, Phase 1 includes 18,000 NVIDIA GB300 Grace Blackwell AI supercomputer—announced May 2025 but deployment timeline unspecified [31]
2. **UK**: £1 billion ($1.3 billion) investment commitment by 2030—future commitment, not yet deployed [30]
3. **15+ of the 20 European AI factories**: Announcements vs. reality gap [30]
4. **UAE G42**: Seeking compute capacity from Northern Data (Germany), accessing nearly half of Northern Data's 23,000 NVIDIA GPUs—deal "nearing completion" as of July 2025, but UAE company is BUYING capacity from European providers, not deploying NVIDIA infrastructure domestically [32]

**The Announcement-to-Deployment Gap**: NVIDIA excels at securing government MOUs and announcements, but actual deployment timelines are often 2-5 years out. Many "deals" are investment commitments, not purchase orders, and revenue recognition is delayed significantly from announcement dates.

### Geopolitical Challenges

**Export Controls**: US restrictions limit deployments in Middle East and China. In August 2023, the US restricted exports of some NVIDIA chips to Middle East countries [32], directly impacting sovereign AI deployments in UAE and Saudi Arabia. This creates uncertainty around which chips can be deployed where.

**The "AI Cold War" Context**: China holds 9 of top 10 spots for open source AI models, while the US dominates proprietary models [33]. Export controls are DRIVING development of NVIDIA alternatives—Huawei, Alibaba, and Baidu are developing alternative AI chips [33]. Countries are caught between US and China ecosystems, with export controls limiting NVIDIA's addressable market and creating opportunities for competitors in restricted markets.

### Competitor Activity

**Huawei**: Developing domestic AI infrastructure for China, serving as "national champion" for Chinese sovereign AI. Export controls have ACCELERATED Huawei's AI chip development [33].

**European Alternatives**: Mistral AI (France) is positioned as European AI champion with open-source focus, pursuing a "partner and build" strategy to leverage EU AI Act for regulatory advantage and achieve European sovereignty without full US dependency [30][33].

**Other National Champions**: Qualcomm (edge AI), Intel (AI accelerators), Alibaba, Baidu, Tencent (Chinese cloud and AI infrastructure). The ecosystem is fragmenting, not consolidating around NVIDIA [33].

### Challenges to the Narrative

1. **Export Control Constraints**: US restrictions limit deployments and create uncertainty, driving development of alternatives
2. **Local Alternatives Emerging**: China's open source model dominance provides free alternatives; European push for regional champions
3. **Cost Concerns**: Sovereign AI requires massive capital investment and energy costs (100+ TWh projected increase) [33]
4. **Talent Scarcity**: China and USA have 60%+ of AI talent; other countries struggle to build domestic expertise [33]
5. **The "Sovereignty Paradox"**: Countries want AI sovereignty but depend on US chips; export controls undermine sovereignty promise; true sovereignty requires full-stack independence (impossible for most)

### Revenue Reality

**What We Found**:
- EMEA Market: $7.6 billion in Q4 2024, growing "almost as quickly as North American market" [30]
- Sovereign AI revenue breakdown: NOT disclosed separately in earnings
- Most deals are multi-year commitments, not immediate revenue

**What We DIDN'T Find**:
- No specific "Sovereign AI" revenue segment in NVIDIA earnings
- No evidence that sovereign AI revenue is material yet
- No data showing sovereign AI offsetting China losses
- Multiple financial sources blocked (403 errors) when searching for China revenue impact

### Verdict: Real But Early Stage

NVIDIA's Sovereign AI strategy is **REAL but EARLY STAGE**. The company has secured impressive government commitments and partnerships, but most are announcements for future deployment (2-5 years out). Actual operational deployments are limited to a handful of European projects (Germany, France).

**Validation of Confidence**: The strategy shows promise with confirmed European deployments and massive Middle East commitments, suggesting NVIDIA's confidence has some basis in reality.

**Cracks in the Narrative**: Export controls undermine the sovereignty promise, most deals are multi-year commitments rather than current revenue, and the fundamental paradox remains—true AI sovereignty requires independence from US technology, which NVIDIA cannot provide. The strategy faces significant headwinds from export controls, emerging competitors, and the fact that revenue from sovereign AI is not yet material (buried in data center segment).

---

## Overall Assessment: Three Bets, Three Different Realities

### Automotive: **Failing** ❌
- Revenue declining (down 4% YoY in Q4 FY2024)
- Competitors growing faster (Qualcomm up 31%)
- Major customers going in-house (Tesla)
- No competitive moat (CUDA irrelevant in automotive)
- Partnership deployments unclear or delayed
- **Gap between fact and reality: WIDE**

### Data Center: **Dominant but Threatened** ⚠️
- 217% revenue growth validates dominance
- 70-95% market share confirmed
- BUT: AMD winning major deployments (173K chips at Meta)
- BUT: Hyperscalers investing $8B+/year in custom chips
- BUT: DOJ antitrust investigation underway
- BUT: Margin compression (66.4% → 64.5%)
- **Gap between fact and reality: NARROW but GROWING**

### Sovereign AI: **Promising but Premature** ⏳
- Impressive government commitments secured
- 2-3 European deployments operational
- Most deals are 2-5 year commitments, not current revenue
- Export controls undermine sovereignty promise
- No evidence of offsetting China losses yet
- **Gap between fact and reality: MODERATE**

### The Bottom Line

NVIDIA's confidence is **most justified in Data Center** (current dominance real), **least justified in Automotive** (struggling against fierce competition), and **premature in Sovereign AI** (future opportunity, not current reality). The company's public narrative consistently emphasizes strengths while downplaying competitive threats and execution challenges. Investors should recognize that while Data Center remains a fortress, the walls are under siege, Automotive is a distraction, and Sovereign AI is a long-term bet that may or may not pay off.

---

## Sources

[1] NVIDIA Press Release, May 24, 2023: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2024

[2] NVIDIA 10-K FY2023, Page 6 - Automotive Section

[3] NVIDIA 10-Q FY2024 Q1, Page 24-25 - Market Platform Highlights

[4] NVIDIA 10-Q FY2024 Q2, Page 31 - Market Platform Highlights

[5] NVIDIA 10-Q FY2024 Q3, Page 35 - Market Platform Highlights

[6] NVIDIA 10-K FY2023, Page 36 - Fiscal Year 2023 Summary

[7] NVIDIA 10-K FY2022, Page 19 - Risk Factors

[8] Forbes - "Is Nvidia Lagging In High-Growth Automotive Segment?" by Steve McDowell (February 22, 2024): https://www.forbes.com/sites/stevemcdowell/2024/02/22/is-nvidia-lagging-in-high-growth-automotive-segment/

[9] Dr. Robert Castellano's Semiconductor Deep Dive - "Nvidia's Dominance in ADAS Processors" (December 25, 2024): https://drrobertcastellano.substack.com/p/nvidias-dominance-in-adas-processors

[10] NVIDIA 10-K FY2023, Page 17 - Competition Risks

[11] CNBC - "Mercedes-Benz partners with Nvidia on upgradable vehicles starting in 2024" (June 23, 2020): https://www.cnbc.com/2020/06/23/mercedes-benz-partners-with-nvidia-on-upgradable-vehicles.html

[12] NVIDIA 10-K FY2024, Page 5 - Business Overview

[13] NVIDIA 10-K FY2024, Page 35 - Market Platform Highlights

[14] American Action Forum - "The DOJ and Nvidia: AI Market Dominance and Antitrust Concerns" (October 7, 2024): https://www.americanactionforum.org/insight/the-doj-and-nvidia-ai-market-dominance-and-antitrust-concerns/

[15] NVIDIA 10-K FY2023, Page 7 - Business Strategies

[16] NVIDIA 10-K FY2023, Page 5 - Data Center Market Overview

[17] NVIDIA 10-Q FY2024 Q1, Page 25 - Market Platform Highlights

[18] NVIDIA 10-Q FY2024 Q2, Page 31 - Market Platform Highlights

[19] NVIDIA 10-K FY2024, Page 8 - Competition

[20] NVIDIA 10-K FY2024, Page 14 - Competition Risk Factors

[21] NVIDIA 10-Q FY2024 Q2, Page 27 - Concentration of Revenue

[22] Constellation Research - "With Oracle Cloud win, AMD MI300X gains traction as Nvidia counterweight" (September 27, 2024): https://www.constellationr.com/blog-news/insights/oracle-cloud-win-amd-mi300x-gains-traction-nvidia-counterweight

[23] Data Gravity - "Hyperscaler AI Custom Chips (ASIC), CPUs and Networking Initiatives" (May 14, 2024): https://www.datagravity.dev/p/hyperscaler-ai-custom-chips-asic

[24] Mercury Technology - "Nvidia Diversifies Beyond Big Tech with Strategic Partnerships" (May 18, 2025): https://mtsoln.com/blog/ai-news-727/nvidia-seeks-to-build-its-business-beyond-big-tech-2461

[25] Barchart/Legacy Grain - "Nvidia Fights Back Against 'Supply Constraint' Rumors" (September 3, 2024): https://www.legacygrain.com/news/story/34576421/nvidia-fights-back-against-supply-constraint-rumors-should-you-buy-the-dip-in-nvda-stock-now

[26] NVIDIA 10-K FY2024, Page 34 - Global Trade

[27] NVIDIA Global Public Sector - National Transformation With Sovereign AI: https://www.nvidia.com/en-us/industries/global-public-sector/

[28] Gulf News - "World Government Summit 2024: Every country must build sovereign AI infrastructure, says Nvidia CEO Jensen Huang": https://gulfnews.com/uae/world-government-summit-2024-in-dubai-every-country-must-build-sovereign-ai-infrastructure-says-nvidia-ceo-jensen-huang-1.101023366

[29] NVIDIA 10-Q Quarter Ended October 29, 2023, Page 31 - Global Trade Section

[30] Futurum Group - "NVIDIA's European AI Sovereignty Push—Report Summary" (June 2025): https://futurumgroup.com/press-release/nvidias-european-ai-sovereignty-push-infrastructure-partnerships-and-policy-report-summary/

[31] NVIDIA Newsroom - "HUMAIN and NVIDIA Announce Strategic Partnership to Build AI Factories of the Future in Saudi Arabia" (May 2025): https://nvidianews.nvidia.com/news/humain-and-nvidia-announce-strategic-partnership-to-build-ai-factories-of-the-future-in-saudi-arabia

[32] Data Center Knowledge - "Abu Dhabi's G42 Close to AI Compute Deal With Northern Data" (July 2025): https://www.datacenterknowledge.com/deals/abu-dhabis-g42-close-to-ai-compute-deal-with-northern-data

[33] Forbes - "The AI Cold War And The Race For Sovereign AI" (November 2025): https://www.forbes.com/sites/johnsviokla/2025/11/18/the-ai-cold-war-and-the-race-for-sovereign-ai/
