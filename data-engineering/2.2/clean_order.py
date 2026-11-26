raw = "  ORD-7001 | 3 | 150,50  "

parts = raw.split("|")
order_id = parts[0].strip()
qty = int(parts[1].strip())
price = float(parts[2].strip().replace(",", "."))

total = qty * price
print(f"{order_id} | {qty} × {price} = {total:.2f} جنيه")
