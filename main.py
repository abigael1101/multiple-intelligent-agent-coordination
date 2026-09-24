"""
Main CLI Application & Demonstration Runner.
Demonstrates the Multiple Intelligent Agent Coordination Strategy for Categorizing and Searching Appropriate Cloud Services.
"""

import sys
import json
import time
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from core.message_bus import MessageBus
from core.search_engine import CloudSearchEngine
from core.llm_adapter import LLMAdapter
from agents import (
    CoordinatorAgent,
    CategorizationAgent,
    SearchAgent,
    CostAgent,
    ComplianceAgent,
    SynthesisAgent
)

# Terminal Styling Helpers
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_banner():
    banner = f"""
{CYAN}{BOLD}========================================================================================
   MULTIPLE INTELLIGENT AGENT COORDINATION FOR CLOUD SERVICE CATEGORIZATION & SEARCH
   Real-World AI Multi-Agent System | FIPA-ACL Protocol | Hybrid Semantic Search
========================================================================================{RESET}
"""
    print(banner)

def load_system() -> CoordinatorAgent:
    """Initialize central message bus, search engine, LLM adapter, and all specialized agents."""
    bus = MessageBus()
    search_engine = CloudSearchEngine()
    llm_adapter = LLMAdapter()

    # Instantiate specialized agents (they auto-register with bus)
    CategorizationAgent("categorization_agent", bus, llm_adapter)
    SearchAgent("search_agent", bus, search_engine)
    CostAgent("cost_agent", bus, llm_adapter)
    ComplianceAgent("compliance_agent", bus, llm_adapter)
    SynthesisAgent("synthesis_agent", bus, llm_adapter)
    
    # Instantiate coordinator supervisor
    coordinator = CoordinatorAgent("coordinator_agent", bus)
    return coordinator

def display_coordination_trace(result: dict):
    """Render human-readable multi-agent trace and final recommendation blueprint."""
    print(f"\n{BOLD}{MAGENTA}[MULTI-AGENT COORDINATION PROTOCOL AUDIT]{RESET}")
    print(f"{'-'*88}")
    
    messages = result.get("message_history", [])
    for idx, msg in enumerate(messages, 1):
        sender = msg["sender"]
        receiver = msg["receiver"]
        performative = msg["performative"]
        t = msg["formatted_time"]
        
        color = CYAN
        if performative == "REQUEST":
            color = YELLOW
        elif performative == "PROPOSE":
            color = GREEN
        elif performative == "CRITIQUE":
            color = RED
        elif performative == "ACCEPT":
            color = GREEN
        elif performative == "SYNTHESIZE":
            color = MAGENTA

        print(f"[{t}] {BOLD}Step {idx:02d}:{RESET} {color}{performative:<10}{RESET} | {sender:<20} -> {receiver:<20}")
        if performative == "REQUEST":
            keys = list(msg["content"].keys())
            print(f"       -> Action Request with payload keys: {keys}")
        elif performative == "INFORM":
            if "requirements" in msg["content"]:
                reqs = msg["content"]["requirements"]
                print(f"       -> Extracted Categories: {reqs.get('detected_categories')} | Workload: {reqs.get('workload_type')}")
            elif "blueprint" in msg["content"]:
                bp = msg["content"]["blueprint"]
                print(f"       -> Synthesized Blueprint: '{bp.get('architecture_title')}' with {len(bp.get('recommended_services', []))} services.")
        elif performative == "PROPOSE":
            cnt = msg["content"].get("count", 0)
            print(f"       -> Proposed {cnt} ranked candidate cloud services.")
        elif performative == "CRITIQUE":
            if "cost_report" in msg["content"]:
                rep = msg["content"]["cost_report"]
                print(f"       -> FinOps Verdict: {rep.get('financial_verdict')} (Warnings: {len(rep.get('cost_critiques', []))})")
            elif "compliance_report" in msg["content"]:
                rep = msg["content"]["compliance_report"]
                print(f"       -> Compliance Verdict: {rep.get('compliance_verdict')} (Security Score: {rep.get('security_score')}%)")

    # Display Categorization Summary
    print(f"\n{BOLD}{CYAN}--- 1. CATEGORIZATION & INTENT DECOMPOSITION ---{RESET}")
    reqs = result.get("categorized_requirements", {})
    print(f"  * Workload Archetype   : {reqs.get('workload_type')}")
    print(f"  * Detected Domains     : {', '.join(reqs.get('detected_categories', []))}")
    print(f"  * Regulatory Mandates  : {', '.join(reqs.get('required_compliance', ['None / Standard']))}")
    print(f"  * Budget Profile       : {reqs.get('cost_preference')}")
    print(f"  * Latency Bound (SLA)  : {reqs.get('latency_sla')}")
    print(f"  * Scale Profile        : {reqs.get('scale_profile')}")

    # Display Top Ranked Services
    print(f"\n{BOLD}{GREEN}--- 2. RETRIEVED & RANKED CLOUD SERVICES ---{RESET}")
    candidates = result.get("candidate_services", [])
    print(f"  {'#':<3} {'Service Name':<26} {'Provider':<10} {'Category':<16} {'Score':<8} {'Cost Tier':<14} {'Compliance'}")
    print(f"  {'-'*95}")
    for idx, s in enumerate(candidates, 1):
        scores = s.get("scores", {})
        comp_str = ", ".join(s.get("compliance", [])[:3])
        print(f"  {idx:<3} {s.get('name')[:25]:<26} {s.get('provider')[:9]:<10} {s.get('category')[:15]:<16} {scores.get('composite', 0)}%     {s.get('cost_tier')[:13]:<14} {comp_str}")

    # Display Multi-Agent Critique
    print(f"\n{BOLD}{YELLOW}--- 3. MULTI-AGENT CRITIQUE & DELIBERATION ---{RESET}")
    cost = result.get("cost_analysis", {})
    comp = result.get("compliance_verification", {})
    print(f"  * FinOps Verdict      : {cost.get('financial_verdict')} (Est: {cost.get('cost_tier_estimate')})")
    for cr in cost.get("cost_critiques", []):
        print(f"    - [Cost Warning] {cr.get('service')}: {cr.get('issue')}")
    for opt in cost.get("finops_recommendations", []):
        print(f"    + [FinOps Pro] {opt.get('service')}: {opt.get('advantage')}")

    print(f"  * Security Verdict    : {comp.get('compliance_verdict')} (Adherence: {comp.get('security_score')}%)")
    for audit in comp.get("audit_trail", [])[:3]:
        print(f"    - [{audit.get('status')}] {audit.get('service')}: {audit.get('details')}")

    # Display Final Architecture Blueprint
    print(f"\n{BOLD}{MAGENTA}--- 4. SYNTHESIZED ARCHITECTURE BLUEPRINT ---{RESET}")
    blueprint = result.get("architecture_blueprint", {})
    print(f"  Title: {BOLD}{blueprint.get('architecture_title')}{RESET}")
    print(f"  Cloud Providers: {', '.join(blueprint.get('primary_provider_mix', []))}")
    print("\n  Dataflow Pipeline:")
    for step in blueprint.get("dataflow_pipeline", []):
        print(f"    [{step.get('step')}] {step.get('service')} ({step.get('provider')}) -> {step.get('tier')} Tier: {step.get('description')}")

    print(f"\n  Mermaid Architecture Diagram:\n")
    print(blueprint.get("mermaid_diagram"))
    print(f"\n{GREEN}{BOLD}Execution Completed in {result.get('execution_time_seconds')} seconds.{RESET}\n")

def run_scenario(scenario_idx: int):
    """Run a predefined benchmark scenario."""
    benchmarks_path = BASE_DIR / "data" / "benchmark_queries.json"
    with open(benchmarks_path, "r", encoding="utf-8") as f:
        scenarios = json.load(f)

    if scenario_idx < 0 or scenario_idx >= len(scenarios):
        print(f"{RED}Invalid scenario index!{RESET}")
        return

    scenario = scenarios[scenario_idx]
    print(f"\n{YELLOW}{BOLD}>>> Running Scenario [{scenario_idx+1}/{len(scenarios)}]: {scenario['title']}{RESET}")
    print(f"Prompt: {scenario['description']}\n")

    coordinator = load_system()
    result = coordinator.run_coordination_cycle(scenario["description"])
    display_coordination_trace(result)

    # Save artifact
    output_path = BASE_DIR / "last_run_result.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"{CYAN}Saved complete multi-agent execution record to: {output_path.name}{RESET}")

def main():
    print_banner()
    benchmarks_path = BASE_DIR / "data" / "benchmark_queries.json"
    with open(benchmarks_path, "r", encoding="utf-8") as f:
        scenarios = json.load(f)

    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        run_scenario(int(sys.argv[1]) - 1)
        return

    print("Select a real-world scenario to demonstrate multi-agent coordination:\n")
    for idx, s in enumerate(scenarios, 1):
        print(f"  [{idx}] {BOLD}{s['title']}{RESET}")
        print(f"      {s['description'][:95]}...\n")
    print("  [C] Custom Requirement Input")
    print("  [Q] Exit")

    choice = input("\nEnter choice [1-5, C, or Q] (Default: 1): ").strip()
    if choice.upper() == "Q":
        print("Exiting.")
        return
    elif choice.upper() == "C":
        custom_prompt = input("\nEnter your real-world cloud system requirements:\n> ").strip()
        if not custom_prompt:
            print("Empty input. Exiting.")
            return
        coordinator = load_system()
        result = coordinator.run_coordination_cycle(custom_prompt)
        display_coordination_trace(result)
    else:
        idx = int(choice) - 1 if choice.isdigit() and 1 <= int(choice) <= len(scenarios) else 0
        run_scenario(idx)

if __name__ == "__main__":
    main()
