"""
Zero-Dependency Web Server & REST API for Multi-Agent Demonstration.
Uses Python standard library (http.server) to provide guaranteed 1-click execution.
"""

import http.server
import socketserver
import json
import urllib.parse
import sys
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

PORT = 8080
UI_DIR = BASE_DIR / "ui"

def init_system() -> CoordinatorAgent:
    bus = MessageBus()
    search_engine = CloudSearchEngine()
    llm_adapter = LLMAdapter()

    CategorizationAgent("categorization_agent", bus, llm_adapter)
    SearchAgent("search_agent", bus, search_engine)
    CostAgent("cost_agent", bus, llm_adapter)
    ComplianceAgent("compliance_agent", bus, llm_adapter)
    SynthesisAgent("synthesis_agent", bus, llm_adapter)
    
    return CoordinatorAgent("coordinator_agent", bus)

class AgentWebHandler(http.server.SimpleHTTPRequestHandler):
    """Handles REST API calls and serves UI assets."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(UI_DIR), **kwargs)

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        
        # API: Get Benchmark Scenarios
        if parsed_url.path == "/api/scenarios":
            scenarios_file = BASE_DIR / "data" / "benchmark_queries.json"
            with open(scenarios_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._send_json(data)
            return

        # API: Get Cloud Catalog
        elif parsed_url.path == "/api/catalog":
            catalog_file = BASE_DIR / "data" / "cloud_catalog.json"
            with open(catalog_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._send_json(data)
            return

        # API: Get System Status / Agents
        elif parsed_url.path == "/api/agents":
            agents_info = [
                {"id": "coordinator_agent", "name": "Coordinator Supervisor", "role": "Orchestrator", "color": "#8b5cf6"},
                {"id": "categorization_agent", "name": "Categorization Agent", "role": "NLP & Taxonomy", "color": "#06b6d4"},
                {"id": "search_agent", "name": "Search Agent", "role": "Vector IR & Matcher", "color": "#10b981"},
                {"id": "cost_agent", "name": "Cost & FinOps Agent", "role": "Pricing & Waste Critique", "color": "#f59e0b"},
                {"id": "compliance_agent", "name": "Compliance Agent", "role": "Security & Audit", "color": "#ef4444"},
                {"id": "synthesis_agent", "name": "Synthesis Agent", "role": "Chief Cloud Architect", "color": "#ec4899"}
            ]
            self._send_json({"agents": agents_info, "status": "READY"})
            return

        # Serve static UI files
        return super().do_GET()

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)

        # API: Run Multi-Agent Coordination Pipeline
        if parsed_url.path == "/api/analyze":
            content_length = int(self.headers.get("Content-Length", 0))
            body_bytes = self.rfile.read(content_length)
            try:
                payload = json.loads(body_bytes.decode("utf-8"))
                prompt = payload.get("prompt", "").strip()
                if not prompt:
                    self._send_json({"error": "Prompt cannot be empty"}, status=400)
                    return

                coordinator = init_system()
                result = coordinator.run_coordination_cycle(prompt)
                self._send_json(result)
            except Exception as e:
                self._send_json({"error": str(e)}, status=500)
            return

        self._send_json({"error": "Not Found"}, status=404)

    def _send_json(self, data, status=200):
        response_bytes = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)

def start_server(port=PORT):
    handler = AgentWebHandler
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"\n=======================================================")
        print(f" Multi-Agent Cloud Recommender Web Server Running!")
        print(f" URL: http://localhost:{port}")
        print(f" Press Ctrl+C to terminate.")
        print(f"=======================================================\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == "__main__":
    port_arg = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else PORT
    start_server(port_arg)
