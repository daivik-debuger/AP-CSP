FoodItems = ["Pizza", "Burger", "Salad", "Tacos", "Pasta", "Sushi", "Hot Dog", "Ice Cream", "Chicken Wrap", "Donut"]
Prices = [8.99, 6.49, 4.25, 7.50, 5.99, 9.75, 3.99, 2.50, 6.75, 1.99]
NeworOld = ["new", "old", "new", "old", "new", "old", "new", "new", "old", "old"]

new_items = []
under_five = []
combined = []

for i in range(len(FoodItems)):
    if NeworOld[i] == "new":
        new_items.append(FoodItems[i])
        if Prices[i] < 5:
            under_five.append(FoodItems[i])
    combined.append(FoodItems[i][-3:] + str(Prices[i]))

print("The cafeteria has added the following items to the menu:")
print(new_items)
print()
print(under_five)
print()
print(combined)

