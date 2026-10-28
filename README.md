# C. elegans Gene ID Converter & Region Fetcher

Two lightweight, single-file web tools for *Caenorhabditis elegans* genes, linked by a small nav bar at the top of each page:

- **Gene ID Converter** (`index.html`): convert between **WormBase Gene IDs**, **Public Names**, **Sequence Names**, and **Entrez Gene IDs**.
- **Region Fetcher** (`celegans-region-fetcher.html`): download a gene with its flanking genomic sequence as **FASTA** or annotated **GenBank**.

---

## Usage

Clone this repository on your machine, or access it online at [https://wormbase-genename-converter.vercel.app/](https://wormbase-genename-converter.vercel.app/).

### Gene ID Converter

1. Select the **output format**, paste your identifiers (one per line, mixed formats allowed), and click **Convert**.

The mapping table is loaded automatically from the local CSV file on page load.

### Region Fetcher

1. Choose the **file type** (FASTA or GenBank) and **orientation** (gene strand or genome + strand).
2. Enter a gene (WormBase ID, gene name or sequence name) and the 5′ / 3′ flank lengths in bp, then click **Download**.

Sequence and annotation are fetched live from the [Ensembl REST API](https://rest.ensembl.org) (assembly WBcel235), so an internet connection is required.

## Features

### Gene ID Converter

- Mixed-input conversion: Public Name → Sequence Name → WormBase ID → Entrez Gene ID
- Selectable output format (WormBase ID, Public Name, Sequence Name, Entrez Gene ID)
- Paste large gene lists and convert in bulk
- Unrecognized identifiers are listed separately
- Copy results to clipboard or download as a `.txt` file

### Region Fetcher

- Accepts WormBase IDs (`WBGene…`), gene names (`rrf-3`) or sequence names (`F10B5.7`)
- Adjustable upstream / downstream flanks, with quick presets (0, 500 bp, 1, 2, 5 kb)
- Output on the gene strand or the genome + strand
- GenBank files are annotated with the gene, its transcripts (mRNA / misc_RNA) and CDS with protein translations
- Region summary, gene map and file preview before saving; copy to clipboard or save again

## Mapping table

The latest mapping table can be downloaded from [WormBase](https://wormbase.org/tools/mine/simplemine.cgi) by selecting the desired columns and clicking `all genes in this species`. The NCBI Entrez Gene IDs were implemented from [DAVID](https://davidbioinformatics.nih.gov/workspace.html?tool=convertKnown_ws).

## Files

| File | Description |
|------|-------------|
| `index.html` | Gene ID Converter (HTML + CSS + JS, single file) |
| `celegans-region-fetcher.html` | Region Fetcher (HTML + CSS + JS, single file) |
| `Gene_IDs_mapping_table.csv` | Gene ID mapping table |
| `favicon.ico` | Shared favicon |
