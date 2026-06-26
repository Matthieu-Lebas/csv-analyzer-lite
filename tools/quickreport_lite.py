#!/usr/bin/env python3
"""Quick CSV Report — Free Lite Edition. Generate an HTML summary from any CSV."""
import csv, sys
from datetime import datetime

HTML_TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>CSV Report</title>
<style>body{{font-family:Arial,sans-serif;max-width:900px;margin:20px auto;padding:20px;background:#f5f5f5}}
.card{{background:white;border-radius:8px;padding:15px;margin:10px 0;box-shadow:0 2px 4px rgba(0,0,0,.1)}}
h1{{color:#1a1a2e}}h2{{color:#16213e}}table{{width:100%;border-collapse:collapse}}
th{{background:#1a1a2e;color:white;padding:8px;text-align:left}}
td{{padding:6px;border-bottom:1px solid #eee}}
tr:hover{{background:#f0f0f0}}.metric{{font-size:24px;font-weight:bold;color:#0f3460}}</style></head>
<body><h1>CSV Quick Report</h1><p>Generated: {date}</p><h2>Summary</h2>{cards}<h2>Data Preview</h2>{table}</body></html>"""

def generate(filepath):
    with open(filepath, newline='') as f:
        reader = csv.reader(f)
        headers = next(reader, [])
        rows = list(reader)
    
    cards = ""
    for i, col in enumerate(headers):
        vals = [r[i] for r in rows if i < len(r) and r[i].strip()]
        nums = []
        for v in vals:
            try: nums.append(float(v.replace('$','').replace(',','')))
            except: pass
        if nums:
            cards += f'<div class="card"><strong>{col}</strong><div class="metric">{len(nums)} values</div>Min: {min(nums):.2f} | Max: {max(nums):.2f} | Avg: {sum(nums)/len(nums):.2f}</div>'
    
    table = '<table><tr>' + ''.join(f'<th>{h}</th>' for h in headers) + '</tr>'
    for row in rows[:20]:
        table += '<tr>' + ''.join(f'<td>{cell[:100] if cell else ""}</td>' for cell in row) + '</tr>'
    table += '</table>'
    
    return HTML_TEMPLATE.format(date=datetime.now().strftime("%Y-%m-%d %H:%M"), cards=cards, table=table)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Quick CSV Report — Free Lite Edition")
        print("Usage: python3 quickreport_lite.py data.csv [output.html]")
        print("Need advanced metrics? Full Report Builder: https://payhip.com/DataCrafted")
        sys.exit(0)
    html = generate(sys.argv[1])
    out = sys.argv[2] if len(sys.argv) > 2 else "report.html"
    with open(out, 'w') as f: f.write(html)
    print(f"Report saved to {out} — {len(html)} bytes")
    print(f"Want full dashboards? https://payhip.com/DataCrafted")
