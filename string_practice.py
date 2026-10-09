# Ask the user for their information and save each item in a variable
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
street_address = input("Enter your street address: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
zipcode = input("Enter your zipcode: ")

# Print an empty line for spacing
print("\n--- Standard Address Format ---\n")

# Print line 1: First and Last Name
print(first_name + " " + last_name)

# Print line 2: Street Address
print(street_address)

# Create the third line of the address by combining city, state, and zipcode
# Format: City, State Zipcode
third_line = city + ", " + state + " " + zipcode

# Print line 3
print(third_line)

# Print another empty line for spacing
print("\n--- Conditional Statement Result ---\n")

# Get the length (number of characters) of the third line
length_of_third_line = len(third_line)

# Write a conditional statement based on the length
if length_of_third_line < 15:
    print("Your city, state, and zip code are quite short!")
elif length_of_third_line < 25:
    print("Your city, state, and zip code are an average length.")
else:
    print("Your city, state, and zip code are very long!")
