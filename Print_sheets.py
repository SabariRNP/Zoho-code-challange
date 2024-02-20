# Print sheets
# In a printing press, there are four sizes of printing paper used A4, A3, A2, A1. For every order,
# the user will give their desired page size (length and breadth).
# Write a program to get the N orders from user and print the best price to the customer
# Price chart (All size in mm)
# A4 - Rs 10 (210 x 297)
# A3 - Rs 15 (297 x 420)
# A2 - Rs 20 (420 x 594)
# A1 - Rs 25 (594 x 841)
# Input:
# No of orders - 2
# Order 1
# Length - 200
# Breadth - 250
# Order 2
# Length - 400
# Breadth - 250
# Output
# Rs 25

sheets = {
    "A4" : {"length": 210, "breath" : 297, "price": 10},
    "A3" : {"length": 297, "breath" : 420, "price": 15},
    "A2" : {"length": 420, "breath" : 594, "price": 20},
    "A1" : {"length": 594, "breath" : 841, "price": 25},
}

nOrders = int(input("Enter number of orders: "))

orders = []
prices = []

for i in range(nOrders):
    print("Order ", i+1)
    len = int(input("Length: "))
    breath = int(input("Breadth: "))
    orders.append((len, breath))
    
print("Orders: ", orders)
for order in orders:
    sortedSizes = sorted(order)
    print("sortedSizes:" , sortedSizes)
    price = 0
    for sheet in sheets.keys():
        print("Sheet: ", sheet)
        sheetDict = sheets[sheet]
        if((sortedSizes[0] <= sheetDict["length"]) and (sortedSizes[1] <= sheetDict["breath"])):
            price = sheets[sheet]["price"]
            break
    
    prices.append(price)
    
print("Prices for orders : ", prices)
if(prices.count(0) > 0):
    print("Order cannot be accomodated")
    
print("Total Price: Rs.", sum(prices))
    