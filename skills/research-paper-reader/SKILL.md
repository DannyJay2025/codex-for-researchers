---
name: research-paper-reader
description: Read, translate, and structure academic papers with source-grounded outputs. Use when the user provides a paper PDF, DOI, arXiv link, publisher URL, abstract, figure legend, table, pasted paper text, or asks for paper reading notes, bilingual reading, journal club preparation, section-by-section explanation, methods/results extraction, or help understanding a research article.
---

# Research Paper Reader

## Workflow

1. Identify the source type: local file, URL, DOI, abstract, pasted text, figure/table, or partial excerpt.
2. Extract bibliographic details when available: title, authors, venue, year, DOI/arXiv ID, and source path or URL.
3. Preserve source grounding. Separate what the paper states from your interpretation.
4. Read in this order: abstract, introduction, methods, results, figures/tables, discussion, limitations.
5. Produce the smallest useful output for the user's goal. Use the full reading brief only when the user asks for deep reading, journal club, or a reusable note.

## Output Contract

Use clear headings and include:

- Citation header: title, authors, venue/year, DOI or URL when available.
- One-sentence thesis: what the paper claims to contribute.
- Problem and motivation: why the work matters.
- Method map: data, model/assay/design, controls, metrics, and comparison baseline.
- Evidence map: key result, supporting figure/table/section, and interpretation.
- Limitations: stated limitations plus obvious unstated risks, clearly labeled.
- Reuse notes: how the user can cite, adapt, reproduce, or critique the work.
- Follow-up questions: concrete questions for literature search, experiments, or supervisor discussion.

## Grounding Rules

- Do not invent missing metadata, citations, figure contents, sample sizes, methods, or statistics.
- If only an abstract is available, label the output as abstract-only.
- If a claim depends on a figure or table that was not provided, mark it as unverified.
- If the user asks for translation, preserve technical terms and keep equations, gene/protein names, model names, units, and citations unchanged.
- If web access is needed to retrieve a DOI, paper page, or current publication metadata, look it up before asserting details.

## Deep Reading Mode

Use `references/reading-brief.md` when the user asks for a full reading brief, journal club notes, bilingual notes, or a reusable Markdown output.

## Commercial Use Angle

For paid deliverables, return a clean Markdown brief that can be copied into Notion, Obsidian, Google Docs, or a lab knowledge base. Include a short "client-ready summary" only when the user asks for client-facing output.
