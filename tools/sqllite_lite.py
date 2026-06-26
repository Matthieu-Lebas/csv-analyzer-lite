#!/usr/bin/env python3
"""SQL Query Helper — Free Lite Edition. English to SQL in one command."""
import sys

TEMPLATES = {
    "select": "SELECT {columns} FROM {table}",
    "top": "SELECT {columns} FROM {table} ORDER BY {order} DESC LIMIT {limit}",
    "count": "SELECT {group}, COUNT(*) as count FROM {table} GROUP BY {group} ORDER BY count DESC",
    "filter": "SELECT * FROM {table} WHERE {column} {op} {value}",
    "join": "SELECT {columns} FROM {t1} JOIN {t2} ON {t1}.{key} = {t2}.{key}",
    "monthly": """SELECT strftime('%Y-%m', {datecol}) as month, COUNT(*) as count, SUM({amount}) as total FROM {table} GROUP BY month ORDER BY month""",
}

def parse_query(text):
    text = text.lower()
    if "top" in text and "by" in text:
        parts = text.replace("top ","").split(" by ")
        limit = parts[0].strip() if parts[0].strip().isdigit() else "10"
        return TEMPLATES["top"].format(columns="*", table="table_name", order="column", limit=limit)
    elif "count" in text and "by" in text:
        group = text.split("by")[-1].strip().split()[0] if text.split("by")[-1].strip() else "category"
        return TEMPLATES["count"].format(group=group, table="table_name")
    elif "month" in text and "revenue" in text:
        return TEMPLATES["monthly"].format(datecol="date", amount="amount", table="table_name")
    elif "join" in text:
        return TEMPLATES["join"].format(columns="*", t1="table1", t2="table2", key="id")
    else:
        return TEMPLATES["select"].format(columns="*", table="table_name")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("SQL Query Helper — Free Lite Edition")
        print("Usage: python3 sqllite_lite.py "your query in plain English"")
        print("Examples:")
        print("  'top 10 customers by revenue'")
        print("  'count orders by category'")
        print("  'monthly revenue growth'")
        print("Need advanced SQL generation? Full toolkit: https://payhip.com/DataCrafted")
        sys.exit(0)
    
    query = " ".join(sys.argv[1:])
    sql = parse_query(query)
    print(f"Input:  {query}")
    print(f"Output: {sql}")
    print(f"\nTip: The full SQL Query Generator supports PostgreSQL, MySQL, SQL Server, SQLite dialects and complex queries.")
    print(f"Get it at: https://payhip.com/DataCrafted")
