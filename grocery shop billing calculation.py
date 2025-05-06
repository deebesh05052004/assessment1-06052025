
num_of_items = int(input("Enter the number of different items : "))
items= []
total_bill = 0
for i in range(num_of_items):
    print("item : ",i+1)
    name = str(input("Enter the the item name : "))
    price = float(input("Enter the price of the item : "))
    quantity = float(input("Enter the item quantity : "))
    total_price = price*quantity
    total_bill += total_price
    items.append((name,price,quantity,total_price))
print("")
print("")
print("--- DEEBESH SUPERMARKET ---")
print("BILL DETAILS")
for item in items:
    print(f"NAME : {item[0]} | PRICE : {item[1]:.2f} | QUANTITY : {item[2]} | TOTAL : {item[3]}")
print("total bill amount need to be paid : ",total_bill)
