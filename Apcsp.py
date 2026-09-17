print("Welcome to The Silicon Bay Checkout System!")

cart = []
subtotal = 0.0


inventory = {
    "ATmega328P": 500.00,
    "DHT11": 50.00,
    "HC-SR04 ultrasonic": 50.00,
    "16x2 LCD screen": 15.00,
    "SG90 servo motor": 10.00,
    "Arduino opta wifi": 250.00,
    "Arduino Pro opta D1608E": 140.90,
    "Arduino Pro opta D1608E Expansion module": 193.35,
    "Raspberry Pi 5": 305.00,
    "Raspberry Pi M.2 HAT+": 25.00,
    "PCIe to 2-ch SATA adapter for raspberry Pi 5": 35.00,
    "Raspberry Pi AI HAT+": 200.00,
    "NA EUV lithography machine from ASML": 400000000.00,
    "ASML high-NA EUV": 350000000.00
}

while True:
    print("\nWelcome to The Silicon Bay!")
    print("1. View Catalog")
    print("2. Add Item to Cart")
    print("3. Remove Item")
    print("4. Change Quantity")
    print("5. View Cart")
    print("6. Checkout")
    
    choice = input("Please select an option (1-6): ")
    
    
    if choice == "1":
        print("\n--- Catalog ---")
        for item in inventory:
            print(item + ": $" + str(inventory[item]))
            
    
    elif choice == "2":
        item_name = input("Enter the exact item name: ")
        
        
        if item_name in inventory:
            quantity_str = input("Enter the quantity: ")
            quantity = int(quantity_str)
            
            
            cart.append([item_name, quantity])
            
            
            subtotal = subtotal + (inventory[item_name] * quantity)
            print("Added to cart!")
        else:
            print("Error: Item not found in inventory.")
            print("Item not found in inventory. Please try again.")
    
    elif choice == "3":
        item_name = input("Enter the item name to remove: ")
        
        found = False
        for i in range(len(cart)):
            
            if cart[i][0] == item_name:
                quantity = cart[i][1]
                
                
                subtotal = subtotal - (inventory[item_name] * quantity)
                
                
                cart.pop(i)
                print("Item removed from cart.")
                found = True
                break
                
        if not found:
            print("Error: Item not found in cart.")
            
    
    elif choice == "4":
        item_name = input("Enter the item name to change quantity: ")
        
        found = False
        for i in range(len(cart)):
            if cart[i][0] == item_name:
                new_quantity_str = input("Enter the new quantity: ")
                new_quantity = int(new_quantity_str)
                
                subtotal = subtotal - (inventory[item_name] * cart[i][1])
                cart[i][1] = new_quantity
                subtotal = subtotal + (inventory[item_name] * new_quantity)
                
                print("Quantity updated!")
                found = True
                break
                
        if not found:
            print("Error: Item not found in cart.")
            
    
    elif choice == "5":
        print("\n--- View Cart ---")
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            for item in cart:
                print(item[0] + " - Quantity: " + str(item[1]))
        print("Current Subtotal: $" + str(subtotal))
        
    
    elif choice == "6":
        
        tax = subtotal * 0.023
        
        
        grand_total = subtotal + tax
        
        
        print("\n--- Itemized Receipt ---")
        for item in cart:
            item_name = item[0]
            quantity = item[1]
            cost = inventory[item_name] * quantity
            print(item_name + " (x" + str(quantity) + "): $" + str(cost))
            
        print("------------------------")
        print("Subtotal: $" + str(round(subtotal, 2)))
        print("Tax (2.3%): $" + str(round(tax, 2)))
        print("Grand Total: $" + str(round(grand_total, 2)))
        

        break
        
    else:
        print("Invalid choice. Please enter 1-6.")
print("This will be deileverd in 500 - 600 business days")
print(print("Thank you for shopping at The Silicon Bay!"))

