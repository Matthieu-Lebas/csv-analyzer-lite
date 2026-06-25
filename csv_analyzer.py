#!/usr/bin/env python3
"""
CSV Analyzer — Open Source Light Edition
=========================================
Drop any CSV file and get instant statistical analysis.
Free version. For the full pipeline with dashboard-ready CSV output,
visit: https://payhip.com/DataCrafted

Usage: python3 csv_analyzer.py your_data.csv
"""
import csv
import sys
from collections import Counter

def analyze_csv(filepath):
    """Analyze a CSV file and print a statistical summary."""
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    
    print(f"\n{'='*60}")
    print(f"  CSV ANALYZER — Statistical Report")
    print(f"  File: {filepath}")
    print(f"  Rows: {len(rows)} | Columns: {len(headers)}")
    print(f"{'='*60}\n")
    
    for col_idx, header in enumerate(headers):
        values = [r[col_idx] for r in rows if col_idx < len(r) and r[col_idx].strip()]
        
        if not values:
            print(f"  [{header}] — empty column, skipping")
            continue
        
        # Detect if numeric
        try:
            nums = [float(v.replace(',','').replace('$','').replace('%','').replace('€','')) 
                    for v in values]
            
            print(f"  [{header}]")
            print(f"    Type: Numeric")
            print(f"    Count: {len(nums)}")
            print(f"    Sum: {sum(nums):,.2f}")
            print(f"    Mean: {sum(nums)/len(nums):,.2f}")
            print(f"    Min: {min(nums):,.2f}")
            print(f"    Max: {max(nums):,.2f}")
            print(f"    Missing: {len(rows) - len(values)}")
            print()
        except ValueError:
            # Text column
            uniq = Counter(values)
            top3 = uniq.most_common(3)
            print(f"  [{header}]")
            print(f"    Type: Text")
            print(f"    Unique values: {len(uniq)}")
            print(f"    Top values: {', '.join(f'{k} ({v})' for k,v in top3)}")
            print(f"    Missing: {len(rows) - len(values)}")
            print()
    
    print(f"{'='*60}")
    print(f"  Want the full pipeline?")
    print(f"  Auto-generated dashboard CSV + extended stats + batch processing")
    print(f"  Get it at: https://payhip.com/DataCrafted")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("CSV Analyzer — Free Light Edition")
        print("Usage: python3 csv_analyzer.py <file.csv>")
        print("\nFull pipeline (dashboard CSV output, batch mode, more stats):")
        print("  https://payhip.com/DataCrafted")
        sys.exit(0)
    
    filepath = sys.argv[1]
    
    # Create sample if requested
    if filepath == "--demo":
        demo_path = "demo_data.csv"
        with open(demo_path, 'w') as f:
            f.write("Month,Revenue,Expenses,Profit,Customers\n")
            f.write("Jan,12500,8200,4300,45\n")
            f.write("Feb,14300,9100,5200,52\n")
            f.write("Mar,11800,7500,4300,38\n")
            f.write("Apr,16200,10200,6000,61\n")
            f.write("May,9800,6400,3400,33\n")
            f.write("Jun,18700,11800,6900,72\n")
        print(f"Demo file created: {demo_path}")
        filepath = demo_path
    
    try:
        analyze_csv(filepath)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        print("Try: python3 csv_analyzer.py --demo")
        sys.exit(1)
