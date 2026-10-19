# 🛡️ ScopeGuard

> A local, privacy-first AI CLI tool that acts as an objective, non-emotional "bad cop" and Technical Project Manager for freelancers, catching contract scope creep and automatically drafting polite Change Order emails.

Built for the **Hacktoberfest Open-Source AI Challenge Week 2: Side Hustle**.
📖 **Read the official submission post & breakdown on DEV.to:** https://dev.to/arceuzvx/i-built-a-local-ai-bad-cop-because-i-suck-at-saying-no-to-freelance-scope-creep-53jc

---

## 💡 The Problem
Freelancers lose thousands of dollars every year to "quick favors" and gradual scope creep. Tracking contract drift against an original Statement of Work and writing firm, polite pushback emails is exhausting and awkward. Worse, pasting confidential client contracts and unreleased feature specs into cloud AI APIs violates strict non-disclosure agreements (NDAs).

## 🚀 The Solution: ScopeGuard
ScopeGuard runs **100% locally** using open-weight models via **Ollama**. It cross-references your baseline contract (`sow.txt`) with messy client requests (`client_message.txt`), isolates out-of-scope work, and drafts a diplomatic Change Order complete with itemized hour estimates ($75/hr baseline).

- **Zero Cloud Egress:** Your client's proprietary data never leaves `127.0.0.1`. Fully NDA compliant.
- **Zero API Costs:** Runs locally on your hardware for $0.00 per run.
- **Local Telemetry:** Instrumented with **Sentry SDK** to monitor local inference latency.

---

## 🛠️ Tech Stack
- **Core:** Python 3.11+
- **Local AI Engine:** Ollama (`qwen3:14b` / `gemma:2b`)
- **Terminal UI:** Rich (Pitch-black & blood-red CLI aesthetic)
- **Telemetry:** Sentry SDK (Transaction tracing)

---

## ⚙️ Quickstart

### 1. Prerequisites
Make sure you have [Ollama](https://ollama.com) installed and running in your background tray, with a model pulled:
```bash
ollama pull qwen3:14b
# or: ollama pull gemma:2b
```

### 2. Clone & Install Dependencies
```bash
git clone [https://github.com/arceuzvx/ScopeGuard.git](https://github.com/arceuzvx/ScopeGuard.git)
cd ScopeGuard
pip install -r requirements.txt
```

### 3. Configure Input Files
Edit sow.txt with your original Statement of Work, and client_message.txt with your client's latest unbilled feature request.

### 4. Run ScopeGuard
```bash
python scopeguard.py
```
