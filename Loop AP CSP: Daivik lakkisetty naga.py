# Name: Daivik lakkisetty naga
# AP CSP - Cookie Sales Loops Assignment

# Two lists: one for the student names and one for how many boxes they sold
students = ["John", "Sophie", "Liam", "Zoe", "Caleb"]
cookie_boxes = [8, 15, 12, 6, 20]

# 1. Calculate Total Sales
# Adding all the cookie boxes together using sum
total_sales = sum(cookie_boxes)
print("Total cookie boxes sold:", total_sales)

# 2. Identify Top Sellers
# Go through the list and print anyone who sold more than 10 boxes
print("\nTop Sellers:")
for i in range(len(students)):
    if cookie_boxes[i] > 10:
        print(students[i])

# 3. Find Students Below Their Goal
# Go through the list and print anyone who sold less than 10 boxes, plus how many they sold
print("\nStudents Below Goal:")
for i in range(len(students)):
    if cookie_boxes[i] < 10:
        print(students[i], "-", cookie_boxes[i], "boxes")

# 4. Search for a Student
# Ask the user to type in a student name
search_name = input("\nEnter a student's name: ").strip()

# Loop through to check if the student is in the list
# We use .lower() on both sides so it works even if the user types in all lowercase or uppercase
found = False
for i in range(len(students)):
    if students[i].lower() == search_name.lower():
        print(students[i], "sold", cookie_boxes[i], "boxes.")
        found = True
        break

# If we checked everyone and didn't find the name
if not found:
    print("Student not found")
    