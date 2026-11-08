FoodItems = ["Pizza", "Burger", "Salad", "Tacos", "Pasta", "Sushi", "Hot Dog", "Ice Cream", "Chicken Wrap", "Donut"]
Prices = [8.99, 6.49, 4.25, 7.50, 5.99, 9.75, 3.99, 2.50, 6.75, 1.99]
NewOrOld = ["new", "old", "new", "old", "new", "old", "new", "new", "old", "old"]


new_items = []
for i in range(len(FoodItems)):
    if NewOrOld[i] == "new":
        new_items.append(FoodItems[i])

print("The cafeteria has added the following items to the menu:")
print(new_items)


cheap_new_items = []
for i in range(len(FoodItems)):
    if NewOrOld[i] == "new" and Prices[i] < 5:
        cheap_new_items.append(FoodItems[i])

print(cheap_new_items)
e

combined_list = []
for i in range(len(FoodItems)):
    suffix = FoodItems[i][-3:]
    combined_list.append(suffix + str(Prices[i]))

print(combined_list)
