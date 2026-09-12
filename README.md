# Trace

An evidence-first research workspace for turning complex questions into answers people can inspect and verify.

## Live site

[Open Trace](https://trace-evidence-research.richa-tigiripally.chatgpt.site/)

## What Trace does

- breaks a research question into specific evidence needs;
- keeps conclusions connected to their supporting evidence; and
- presents reviewed RAG experiment results with their limitations, rather than treating a promising oracle result as an automated-system result.

## RAG research results

Trace reads its reviewed experiment data from [`research/experiment-results.json`](research/experiment-results.json). The data is exported from the local `reasoning-unit-rag` experiment reports with:

```bash
python tools/export_rag_results.py \
  --experiments-dir /path/to/reasoning-unit-rag/experiments \
  --output research/experiment-results.json \
  --published-output dist/research/experiment-results.json
```

This produces the reviewed source data and the file served by the site from the same payload.

## Project structure

- `dist/` — the static Trace site
- `research/` — reviewed experiment-result data and notes
- `tools/` — data-export utilities
