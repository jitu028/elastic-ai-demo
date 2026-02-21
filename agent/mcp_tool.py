from agent.mcp_client import MCPClient
from agent.llm import safe_generate
from rich.console import Console
from rich.panel import Panel
import os
import time

console = Console()




def build_doc_topics(incident_analysis: str):
    prompt = f"""
You are converting a cloud security incident into Google Cloud documentation lookup topics.

Return documentation topic phrases only.
Use official product terminology.
No security language.
No attacker wording.

Example:
Bad: attacker gained admin access
Good: IAM role permissions

Incident:
{incident_analysis}
"""

    text = safe_generate(prompt)

    topics = []
    for line in text.split("\n"):
        line = line.strip("- ").strip()
        if 3 < len(line) < 60:
            topics.append(line)

    return topics[:5]




def lookup_security_guidance(analysis_text: str):
    console.print(Panel("🔎 Querying Google Developer Knowledge MCP", style="blue"))

    mcp = MCPClient()
    topics = build_doc_topics(analysis_text)

    console.print(f"[cyan]Doc Topics:[/cyan] {topics}")

    matched_docs = []

    for topic in topics:
        result = mcp.call_tool("search_documents", {"query": topic})

        if isinstance(result, dict) and "documents" in result:
            for d in result["documents"][:2]:
                if "name" in d:
                    matched_docs.append(d["name"])

    matched_docs = list(set(matched_docs))[:5]

    if not matched_docs:
        return "No relevant official documentation found."

    docs = mcp.call_tool("batch_get_documents", {"names": matched_docs})

    return str(docs)
