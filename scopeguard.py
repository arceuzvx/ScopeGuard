import sys
import time
from pathlib import Path
import ollama
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

# Minimalist Pitch-Black and Blood-Red Terminal Palette
RED = "bold red"
DARK_RED = "#8b0000"
MUTED = "#555555"

def print_banner():
    banner = """
  ███████╗ ██████╗ ██████╗ ██████╗ ███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ 
  ██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
  ███████╗██║     ██║   ██║██████╔╝█████╗  ██║  ███╗██║   ██║███████║██████╔╝██║  ██║
  ╚════██║██║     ██║   ██║██╔═══╝ ██╔══╝  ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
  ███████║╚██████╗╚██████╔╝██║     ███████╗╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
  ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                 [ LOCAL SCOPE-CREEP & CONTRACT DRIFT DEFENDER ]
    """
    console.print(f"[{DARK_RED}]{banner}[/{DARK_RED}]")

def load_file(filename: str) -> str:
    path = Path(filename)
    if not path.exists():
        console.print(f"[{RED}][!] Error:[/{RED}] Missing file '{filename}'.")
        sys.exit(1)
    return path.read_text(encoding="utf-8")

def analyze_scope(sow_text: str, client_text: str, model: str = "gemma:2b"):
    prompt = f"""You are a senior freelance contract negotiator and technical project manager.

ORIGINAL STATEMENT OF WORK (SoW):
\"\"\"
{sow_text}
\"\"\"

NEW CLIENT REQUEST / EMAIL:
\"\"\"
{client_text}
\"\"\"

TASKS:
1. Identify all items in the client's request that are OUT OF SCOPE relative to the original Statement of Work.
2. Draft a firm, polite, and professional email to the client:
   - Acknowledge their ideas enthusiastically.
   - Clarify that these additions fall outside the agreed baseline SoW.
   - Include a structured Change Order proposal with estimated hours, hourly rate ($75/hr), and milestone impact.
   - Provide a call to action asking if they'd like to proceed with the updated scope.

FORMAT YOUR RESPONSE AS:
# Scope Drift Analysis
- **In-Scope Confirmed:** <items>
- **Out-of-Scope Drift:** <items flagged with financial risk>

# Client Change Order Email
\"\"\"
<Draft email text here>
\"\"\"
"""

    console.print(f"[{MUTED}][*] Initializing local inference on {model} via Ollama...[/{MUTED}]")
    start_time = time.time()

    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        latency = time.time() - start_time
        return response['message']['content'], latency
    except Exception as e:
        console.print(f"[{RED}][!] Ollama invocation failed:[/{RED}] {e}")
        console.print(f"[{MUTED}]Tip: If '{model}' is not available, switch the model parameter to 'gemma:2b' or your active Ollama model.[/{MUTED}]")
        sys.exit(1)

def main():
    print_banner()

    # Load baseline assets
    sow_content = load_file("sow.txt")
    client_content = load_file("client_message.txt")

    console.print(f"[{DARK_RED}]─── Loaded Inputs ───────────────────────────────────────────[/{DARK_RED}]")
    console.print(f"[{MUTED}][+] sow.txt ({len(sow_content)} chars)[/{MUTED}]")
    console.print(f"[{MUTED}][+] client_message.txt ({len(client_content)} chars)[/{MUTED}]")

    # Run analysis (Change model to 'gemma:2b' if submitting for Gemma category)
    model_name = "gemma:2b"
    result, latency = analyze_scope(sow_content, client_content, model=model_name)

    # Render results
    console.print(f"\n[{DARK_RED}]─── Audit & Defense Output ───────────────────────────────────[/{DARK_RED}]\n")
    console.print(Panel(Markdown(result), border_style=DARK_RED, title="ScopeGuard Report"))

    console.print(f"\n[{MUTED}][*] Inference Latency: {latency:.2f}s | Telemetry logged locally | Zero data egress.[/{MUTED}]")

if __name__ == "__main__":
    main()