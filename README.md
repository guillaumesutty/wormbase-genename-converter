# C. elegans Gene ID Converter

A lightweight, single-file web tool for converting between **WormBase Gene IDs**, **Public Names**, **Sequence Names**, and **Entrez Gene IDs** in *Caenorhabditis elegans*.

---

## Usage

1. Clone this repository on your machine, or access it online at [https://wormbase-genename-converter.vercel.app/](https://wormbase-genename-converter.vercel.app/)
2. Select the **output format**, paste your identifiers (one per line, mixed formats allowed), and click **Convert**.

The mapping table is loaded automatically from the local CSV file on page load.

## Features

- Mixed-input conversion: Public Name → Sequence Name → WormBase ID → Entrez Gene ID
- Selectable output format (WormBase ID, Public Name, Sequence Name, Entrez Gene ID)
- Paste large gene lists and convert in bulk
- Unrecognized identifiers are listed separately
- Copy results to clipboard or download as a `.txt` file

## Mapping table

The latest mapping table can be downloaded from [WormBase](https://wormbase.org/tools/mine/simplemine.cgi) by selecting the desired columns and clicking `all genes in this species`. The NCBI Entrez Gene IDs were implemented from [DAVID](https://davidbioinformatics.nih.gov/workspace.html?tool=convertKnown_ws).

## Files

| File | Description |
|------|-------------|
| `index.html` | The complete web app (HTML + CSS + JS, single file) |
| `Gene_IDs_mapping_table.csv` | Gene ID mapping table |
