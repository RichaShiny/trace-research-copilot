# Research data contract

`experiment-results.json` is the small, reviewed boundary between Trace and the existing `reasoning-unit-rag` research project.

The first integration deliberately exposes both the positive oracle result and the unsuccessful rule-based baseline. That keeps the product honest: Trace may show evidence and interpret a result, but it must distinguish a promising upper bound from an automated capability.

Next implementation step: add an exporter in `reasoning-unit-rag` that writes this same schema after each evaluation run, then let Trace ingest the exported JSON through a server-side API.
