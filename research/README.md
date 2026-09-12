# Research data contract

`experiment-results.json` is the small, reviewed boundary between Trace and the existing `reasoning-unit-rag` research project.

The first integration deliberately exposes both the positive oracle result and the unsuccessful rule-based baseline. That keeps the product honest: Trace may show evidence and interpret a result, but it must distinguish a promising upper bound from an automated capability.

Refresh it from the local RAG experiment reports with:

```bash
python tools/export_rag_results.py \
  --experiments-dir /path/to/reasoning-unit-rag/experiments \
  --output research/experiment-results.json \
  --published-output dist/research/experiment-results.json
```

The exporter intentionally includes both the positive oracle result and the unsuccessful rule-based baseline. Trace can therefore distinguish a promising upper bound from automated-system performance.
