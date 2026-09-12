# Trace

Trace is an API change monitor for product teams. It turns a technical API update into a simple answer: what changed, who it affects, and what to do next.

## Live demo

[Open Trace](https://trace-evidence-research.richa-tigiripally.chatgpt.site/)

## Live public API checks

Trace can fetch current data from three public sources: GitHub, Open-Meteo, and the USGS earthquake feed. It saves a small local snapshot for each source and explains whether the visible response fields changed on a later check.

The live checks are deliberately credential-free and the snapshots stay in the visitor's browser. A production backend will add shared history, scheduled checks, impact analysis, and notifications.

## Current prototype

This version demonstrates a working live-data flow with public sources. Connecting customer APIs, shared monitoring history, and automated code fixes is the next backend milestone.

## Project structure

- `dist/` — static product interface
