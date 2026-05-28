import argparse
import csv
from collections import defaultdict
from pathlib import Path


def unique_preserve(items):
    seen = set()
    result = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result


def read_entrez_mapping(path):
    entrez_by_wb = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        for row in reader:
            entrez = (row.get("Entrez Gene ID") or "").strip()
            wb_field = (row.get("WormBase Gene ID") or "").strip()
            if not entrez or not wb_field:
                continue
            for wb_id in wb_field.split(","):
                wb_id = wb_id.strip()
                if wb_id:
                    entrez_by_wb[wb_id].append(entrez)
    return entrez_by_wb


def build_output(mapping_path, entrez_path, output_path):
    entrez_by_wb = read_entrez_mapping(entrez_path)

    with mapping_path.open(newline="", encoding="utf-8") as mapping_handle, \
            output_path.open("w", newline="", encoding="utf-8") as output_handle:
        mapping_reader = csv.DictReader(mapping_handle, delimiter=";")
        fieldnames = [
            "WormBase Gene ID",
            "Public Name",
            "Sequence Name",
            "Entrez Gene ID",
        ]
        writer = csv.DictWriter(output_handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()

        for row in mapping_reader:
            wb_id = (row.get("WormBase Gene ID") or "").strip()
            if not wb_id:
                continue
            entrez_list = unique_preserve(entrez_by_wb.get(wb_id, []))
            writer.writerow(
                {
                    "WormBase Gene ID": wb_id,
                    "Public Name": (row.get("Public Name") or "").strip(),
                    "Sequence Name": (row.get("Sequence Name") or "").strip(),
                    "Entrez Gene ID": ",".join(entrez_list),
                }
            )


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Create Gene_IDs_mapping_table.csv with WormBase, Public, Sequence, and Entrez IDs."
        )
    )
    parser.add_argument(
        "--mapping",
        type=Path,
        default=Path("WBid-gene_name_mapping_table.csv"),
        help="Path to WBid-gene_name_mapping_table.csv",
    )
    parser.add_argument(
        "--entrez",
        type=Path,
        default=Path("WBids-Entrez.csv"),
        help="Path to WBids-Entrez.csv",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("Gene_IDs_mapping_table.csv"),
        help="Path to output Gene_IDs_mapping_table.csv",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    build_output(args.mapping, args.entrez, args.output)


if __name__ == "__main__":
    main()
