import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from google import genai

from agent.tools import fetch_security_events
from agent.prompts import SYSTEM_PROMPT
from agent.mcp_tool import lookup_security_guidance
from agent.llm import safe_generate
import time

load_dotenv()
console = Console()


def run_security_agent():

    console.print(Panel.fit("🤖 AI Security Agent Activated", style="bold cyan"))

    # Step 1 — telemetry
    events = fetch_security_events()

    hypothesis_prompt = f"""
{SYSTEM_PROMPT}

Analyze these audit logs and produce a security hypothesis:

{events}
"""

    hypothesis = safe_generate(hypothesis_prompt)

    console.print(Panel(hypothesis, title="AI Hypothesis", style="yellow"))

    # Step 2 — ground with official documentation
    official_guidance = lookup_security_guidance(hypothesis)

    console.print(Panel(official_guidance, title="Official Guidance (MCP)", style="blue"))

    # Step 3 — final grounded report
    final_prompt = f"""
Create a final incident report grounded in official documentation.

AI Findings:
{hypothesis}

Official Documentation:
{official_guidance}

Return structured sections:
- Incident Summary
- Root Cause
- Attack Pattern
- Risk Level
- Remediation Steps
"""

    final_report = safe_generate(final_prompt)

    console.print(Panel(final_report, title="Grounded Security Report", style="bold red"))
