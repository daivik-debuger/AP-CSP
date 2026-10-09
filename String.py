first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
street_address = input("Enter your street address: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
zipcode = input("Enter your zipcode: ")

print("\n========================================")
print("       MAILING ADDRESS     ")
print("========================================")

print("|   Name:    " + first_name + " " + last_name)

print("|  Street:  " + street_address)

third_line = city + ", " + state + " " + zipcode

print("|   Region:  " + third_line)

print("========================================\n")

print(" --- Length Analysis Result --- \n")

length_of_third_line = len(third_line)

if length_of_third_line < 15:
    print(" Your city, state, and zip code are quite short!")
elif length_of_third_line < 25:
    print("Your city, state, and zip code are an average length.")
else:
    print(" Your city, state, and zip code are very long!")
