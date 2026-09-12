#!/usr/bin/env python3
"""Export reviewed reasoning-unit RAG experiment summaries for Trace.

Usage:
  python tools/export_rag_results.py \
    --experiments-dir /path/to/reasoning-unit-rag/experiments \
    --output research/experiment-results.json
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


EXPERIMENTS = (
    {
        "file": "004_reasoning_unit_retrieval.md",
        "id": "004",
        "title": "Rule-based reasoning-unit retrieval",
        "sample_size": 100,
        "retrieval_unit": "passage",
        "baseline_label": "Baseline Passage Retrieval",
        "result_label": "Rule-Based Reasoning Unit Retrieval",
    },
    {
        "file": "006_oracle_sentence_retrieval.md",
        "id": "006",
        "title": "Oracle reasoning units for sentence retrieval",
        "sample_size": 5,
        "retrieval_unit": "sentence",
        "baseline_label": "Original-question retrieval",
        "result_label": "Oracle reasoning-unit retrieval",
    },
)


def recall_for(markdown: str, label: str) -> float:
    pattern = rf"\|\s*{re.escape(label)}\s*\|\s*([0-9.]+)\s*\|"
    match = re.search(pattern, markdown, flags=re.IGNORECASE)
    if not match:
        raise ValueError(f"Could not find a recall row for {label!r}.")
    return float(match.group(1))


def section(markdown: str, heading: str) -> str | None:
    match = re.search(
        rf"^## {re.escape(heading)}\s*\n+(.+?)(?=^## |\Z)",
        markdown,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not match:
        return None
    return " ".join(match.group(1).strip().split())


def export(experiments_dir: Path) -> dict:
    results = []
    for spec in EXPERIMENTS:
        markdown = (experiments_dir / spec["file"]).read_text(encoding="utf-8")
        baseline = recall_for(markdown, spec["baseline_label"])
        result = recall_for(markdown, spec["result_label"])
        experiment = {
            "id": spec["id"],
            "title": spec["title"],
            "sample_size": spec["sample_size"],
            "retrieval_unit": spec["retrieval_unit"],
            "baseline_recall": baseline,
            "reasoning_unit_recall": result,
            "delta": round(result - baseline, 3),
            "finding": section(markdown, "Interpretation"),
        }
        limitations = section(markdown, "Limitations")
        if limitations:
            experiment["limitations"] = limitations
        results.append(experiment)

    return {
        "source_project": "reasoning-unit-rag",
        "dataset": "HotpotQA distractor validation split",
        "updated_at": str(date.today()),
        "experiments": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--experiments-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    payload = export(args.experiments_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
