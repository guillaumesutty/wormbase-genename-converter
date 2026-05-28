# C. elegans Gene ID Converter

A lightweight, single-file web tool for bidirectional conversion between **WormBase Gene IDs** (e.g. `WBGene00004804`) and **gene names** (e.g. `daf-2`) in *Caenorhabditis elegans*.

---

## Usage

1. Clone this repository on your machine, or access it online at [https://wormbase-genename-converter.vercel.app/](https://wormbase-genename-converter.vercel.app/)
3. Select the conversion direction, paste your identifiers (one per line), and click **Convert**.

The mapping table is loaded automatically from the local CSV file on page load.

## Features

- **WBid → Gene name** and **Gene name → WBid** conversion
- Paste large gene lists and convert in bulk
- When converting gene names to WBids, the tool first searches the **Public Name** column; if no match is found, it falls back to the **Sequence Name** column
- Unrecognized identifiers are flagged inline as `[NOT FOUND: ...]` and listed separately
- Copy results to clipboard or download as a `.txt` file

## Mapping table

The latest mapping table can be downloaded from [WormBase](https://wormbase.org/tools/mine/simplemine.cgi) by selecting desired columns and click `all genes in this species`.

## Files

| File | Description |
|------|-------------|
| `index.html` | The complete web app (HTML + CSS + JS, single file) |
| `WBid-gene_name_mapping_table.csv` | Gene ID mapping table |
