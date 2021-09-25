order = input()
order = order.split()

menu = {"Nachos" : 6, "Pizza" : 6, "Cheeseburger" : 10, "Water" : 4, "Coke" : 5}

total = 0
for i in range(len(order)):
    if order[i] in menu.keys():
        total += menu[order[i]]
    else:
        total += menu["Coke"]

print(round(total * 1.07, 2))
