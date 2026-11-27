qty = 7
if qty > 10:
    print("bulk order")
elif qty > 0:
    print("normal order")
else:
    print("invalid quantity")
status = "paid"
if status == "paid" and qty > 0:
    print("ship it")
