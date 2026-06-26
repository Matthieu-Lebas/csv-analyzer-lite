#!/usr/bin/env python3
"""JSON to CSV — Free Lite Edition. Flatten any JSON to CSV in one command."""
import json, csv, sys

def flatten_json(data, prefix=""):
    rows = []
    if isinstance(data, list):
        for item in data:
            rows.extend(flatten_json(item, prefix))
    elif isinstance(data, dict):
        row = {}
        for k, v in data.items():
            key = f"{prefix}.{k}" if prefix else k
            if isinstance(v, (dict, list)):
                sub = flatten_json(v, key)
                if sub:
                    for sr in sub:
                        row.update(sr)
            else:
                row[key] = v
        rows.append(row)
    return rows

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("JSON to CSV — Free Lite Edition")
        print("Usage: python3 json2csv_lite.py data.json [output.csv]")
        print("Get the full version: https://payhip.com/DataCrafted")
        sys.exit(0)
    
    with open(sys.argv[1]) as f:
        data = json.load(f)
    
    rows = flatten_json(data)
    if not rows:
        print("No data found or unsupported format. Try the full JSON-to-CSV Converter at payhip.com/DataCrafted")
        sys.exit(1)
    
    out = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1].replace('.json', '.csv')
    with open(out, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Converted {len(rows)} rows to {out}")
    print(f"Need nested arrays and custom delimiters? Full version: https://payhip.com/DataCrafted")
