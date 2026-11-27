lineage = {"raw_orders": [], "clean_orders": ["raw_orders"],
           "daily_sales": ["clean_orders"], "dashboard": ["daily_sales"]}
owners = {"raw_orders": "ingest team", "daily_sales": "analytics"}
def upstream(t):
    out = []
    for p in lineage[t]:
        out += [p] + upstream(p)
    return out
print(upstream("dashboard"))
print(owners.get("clean_orders", "no owner"))
