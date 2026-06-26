# CSV Analyzer — Light Edition

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DataCrafted](https://img.shields.io/badge/Store-DataCrafted-red.svg)](https://payhip.com/DataCrafted)

Drop any CSV file and get an instant statistical analysis report. **Zero dependencies.** Pure Python.

## Quick Start

```bash
# Try with demo data
python3 csv_analyzer.py --demo

# Analyze your own CSV
python3 csv_analyzer.py your_data.csv
```

## Output

```
==============================================================
  CSV ANALYZER — Statistical Report
  File: sales.csv
  Rows: 6 | Columns: 4
==============================================================

  [Revenue]
    Type: Numeric
    Count: 6
    Sum: 83,300.00
    Mean: 13,883.33
    Min: 9,800.00
    Max: 18,700.00
    Missing: 0

  [Customers]
    Type: Numeric
    Count: 6
    Sum: 301.00
    Mean: 50.17
    Min: 33.00
    Max: 72.00
    Missing: 0
==============================================================
```

## Features

- **Auto-detection** — Numeric vs text columns, currency handling ($, €, %)
- **Instant stats** — Sum, mean, min, max, count, missing data
- **Text analysis** — Unique values, top occurrences
- **Demo mode** — `--demo` flag creates sample data instantly
- **Zero deps** — Runs on Python 3.6+, nothing to install

## Free Tools Included

This repo now includes **4 free Python tools** — all zero-dependency, single-file, ready to use:

| Tool | File | Description |
|------|------|-------------|
| CSV Analyzer | `csv_analyzer.py` | Instant stats from any CSV |
| JSON→CSV | `tools/json2csv_lite.py` | Flatten nested JSON to CSV |
| Quick Report | `tools/quickreport_lite.py` | CSV → styled HTML report |
| SQL Helper | `tools/sqllite_lite.py` | Plain English → SQL query |

```bash
python3 csv_analyzer.py data.csv
python3 tools/json2csv_lite.py data.json
python3 tools/quickreport_lite.py data.csv
python3 tools/sqllite_lite.py "top 10 customers by revenue"
```

## Full Pipeline

Need more power? The **DataCrafted Pro Pipeline** adds:

- 📊 Dashboard-ready CSV output (import straight to Google Sheets)
- 🔄 Batch processing (analyze 100+ files at once)
- 📈 Extended statistics (percentiles, std dev, correlations)
- 🎨 Styled HTML reports
- 📁 Any encoding, any delimiter, any size

**[Get the full pipeline →](https://payhip.com/DataCrafted)**

## Also from DataCrafted

| Tool | Price |
|------|-------|
| Web Scraper Toolkit | $29.99 |
| SQL Query Generator | $29.99 |
| Business Metrics Bundle | $19.99 |
| Automated Report Builder | $34.99 |
| Data Analysis Master Bundle | $49.99 |

**[Visit DataCrafted Store →](https://payhip.com/DataCrafted)**

## License

MIT — Free to use, modify, and distribute.
