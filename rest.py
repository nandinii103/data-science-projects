items = ["pen" , "pencil" , "notebook"]
for row,item in enumerate(items):
    print(row,item)

currency = "POUNDS"
symbol = "£" if currency == "POUNDS" else "$"

quantity = "5"
if quantity.isdigit():
    print("Valid Quantity")
else:
    print("Invalid Quantity")
    