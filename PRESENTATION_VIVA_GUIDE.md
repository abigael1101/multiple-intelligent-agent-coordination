# 5-Minute Demonstration & Viva Examination Guide [5 Marks]

**Topic**: Multiple Intelligent Agent Coordination Strategy for Categorizing and Searching Appropriate Cloud Services  
**Evaluation Rubric**: Demonstration [5M] & Implementation of small part of system using AI tools  

---

## 1. 5-Minute Demonstration Script (Minute-by-Minute)

### **Minute 0:00 - 1:00 | The Problem & Multi-Agent Architecture**
> *"Good morning / afternoon professors. Today I am demonstrating our AI application: a **Multiple Intelligent Agent Coordination System for Categorizing and Searching Appropriate Cloud Services**.*  
>  
> *In enterprise environments, choosing cloud services is challenging because developers must balance conflicting trade-offs: functional requirements, strict regulatory compliance like HIPAA or PCI-DSS, and FinOps budget constraints. A single search bar or generic LLM fails because it cannot negotiate these trade-offs.*  
>  
> *To solve this, we implemented a **Hub-and-Spoke Blackboard Multi-Agent Architecture** with six autonomous specialized agents communicating via the **FIPA-ACL communication protocol**:*  
> 1. *Coordinator Agent (Supervisor & Blackboard Controller)*  
> 2. *Categorization Agent (NLP Intent & Taxonomy Extraction)*  
> 3. *Search Agent (Hybrid Vector TF-IDF Cosine Similarity IR)*  
> 4. *Cost Agent (FinOps & Idle Waste Critique)*  
> 5. *Compliance Agent (HIPAA / PCI / SOC2 Security Auditor)*  
> 6. *Synthesis Agent (Chief Cloud Solutions Architect)*  
> *Let us now see the live multi-agent deliberation in action."*

---

### **Minute 1:00 - 2:30 | Live Demonstration: Scenario 1 (HealthTech HIPAA PHI)**
1. Open the Web Dashboard at `http://localhost:8080` (or run `python main.py 1`).
2. Click on the first benchmark card: **"HealthTech PHI & Medical Image Analysis Pipeline"**.
3. Click **"Trigger Multi-Agent Deliberation"**.
4. **Point to the screen and explain**:
   - *"Notice how the top agent status bar dynamically lights up as each agent takes its turn: Coordinator &rarr; Categorization &rarr; Search &rarr; Cost & Compliance &rarr; Synthesis."*
   - *"In the **Protocol Message Bus Feed**, you can see the formal FIPA-ACL messages being passed: `REQUEST`, `INFORM`, `PROPOSE`, `CRITIQUE`, and `ACCEPT`."*
   - *"Switch to the **Intent & Taxonomy Tab**: The Categorization Agent decomposed the query into an `AI_INFERENCE_PIPELINE`, flagged `HIPAA` as a mandatory regulatory constraint, and detected `Storage` and `AI/ML` as target domains."*
   - *"Switch to the **Ranked Cloud Services Tab**: The Search Agent ranked Amazon SageMaker (58.1%), Bedrock (56.8%), Azure OpenAI (55.9%), and S3 (53.8%). Notice the multi-criteria breakdown bars showing semantic similarity, domain alignment, and compliance."*
   - *"Switch to the **Architecture Blueprint Tab**: The Synthesis Agent compiled an end-to-end dataflow pipeline and generated a clean Mermaid architecture diagram connecting Ingress &rarr; S3 &rarr; SageMaker &rarr; Bedrock."*

---

### **Minute 2:30 - 3:45 | Live Demonstration: Scenario 2 (Multi-Agent Critique & Conflict Resolution)**
1. Click on the second benchmark card: **"Global E-Commerce Flash Sale & Real-time Order Engine"**.
2. Click **"Trigger Multi-Agent Deliberation"**.
3. **Point out the multi-agent critique in action**:
   - *"Notice what happened here in the **FinOps & Compliance Audit Tab**: This is the heart of multi-agent coordination. The user specified a **cost-sensitive** flash sale workload. When the Search Agent proposed Google Cloud Spanner and Amazon RDS, the **Cost Agent intervened with a `CRITIQUE` performative**, warning that Spanner and provisioned RDS incur high baseline idle costs when traffic drops."*
   - *"The Cost Agent suggested serverless scale-to-zero alternatives like Amazon DynamoDB On-Demand and Aurora Serverless, while the Compliance Agent independently verified PCI-DSS payment card data security."*
   - *"This demonstrates true **collaborative multi-agent negotiation**, which a traditional monolithic search engine cannot do."*

---

### **Minute 3:45 - 5:00 | Code Rigor, Zero-Dependency Design & Wrap-Up**
1. Show the terminal running the automated unit test suite:
   ```bash
   python -m unittest discover -s tests -v
   ```
2. Explain:
   - *"Our system includes 7 automated unit and integration tests with 100% pass rate in 0.01 seconds."*
   - *"The entire repository is built with zero external pip dependencies using Python's standard library, ensuring guaranteed portability and instant deployment."*
   - *"Thank you, professors. I am now open to your questions."*

---

## 2. Likely Viva Examination Questions & Model Answers

### Q1: Why use a Multi-Agent System (MAS) instead of a single LLM prompt?
**Model Answer**:  
*"A single LLM prompt suffers from context pollution, hallucination of non-compliant cloud services, and lack of accountability. In a real-world enterprise, architecture design involves competing organizational priorities: Developers want features, the FinOps team wants minimal idle cost, and the CISO enforces compliance. By decoupling these concerns into dedicated, specialized agents (Categorization, Search, Cost, Compliance, Synthesis) that communicate via formal performatives, each agent applies deterministic checks and deep domain rules. This guarantees transparent auditing and conflict resolution."*

### Q2: What is the FIPA-ACL protocol and why did you use it?
**Model Answer**:  
*"FIPA-ACL stands for Foundation for Intelligent Physical Agents - Agent Communication Language. It is the international standard for multi-agent communication. Instead of exchanging arbitrary text strings, agents exchange structured message envelopes containing a sender, receiver, timestamp, conversation ID, and a **performative** that declares the communicative intent (`REQUEST`, `INFORM`, `PROPOSE`, `CRITIQUE`, `ACCEPT`, `SYNTHESIZE`). This formal protocol prevents race conditions and makes the deliberation audit trail explainable."*

### Q3: What is the Blackboard Architecture?
**Model Answer**:  
*"The Blackboard Architecture is an established pattern in AI where independent specialized agents collaborate by reading from and writing to a shared global problem-solving workspace called the Blackboard. In our system, the Blackboard stores the user query, intermediate categorized requirements, candidate service pools, FinOps alerts, and the final synthesized blueprint. The Coordinator Agent acts as the Blackboard controller, orchestrating when each agent inspects and modifies the blackboard state."*

### Q4: How does your Search Agent rank cloud services? What formula is used?
**Model Answer**:  
*"Our Search Agent uses a multi-objective composite scoring formula combining information retrieval and constraint satisfaction:*
$$\text{CompositeScore} = 0.45 \cdot S_{\text{semantic}} + 0.25 \cdot S_{\text{category}} + 0.20 \cdot S_{\text{compliance}} + 0.10 \cdot S_{\text{cost}}$$
*Semantic similarity $S_{\text{semantic}}$ is computed using the dot product of normalized TF-IDF vector embeddings between the query and catalog service metadata. The compliance score enforces mandatory frameworks (e.g. HIPAA, PCI-DSS) as a strict constraint ratio, and the cost score penalizes high idle-tier services for budget-sensitive queries."*

### Q5: Can this system connect to live LLM APIs like Google Gemini or OpenAI?
**Model Answer**:  
*"Yes. In `core/llm_adapter.py`, we implemented an adapter pattern. If the user configures an `OPENAI_API_KEY` or `GEMINI_API_KEY` environment variable, the agents can delegate generative reasoning to external frontier models. However, we also built a comprehensive, zero-dependency **Local AI Engine** inside `llm_adapter.py`. This ensures the system runs deterministically, sub-second, and offline without risk of API rate limits or network downtime during academic evaluations."*
