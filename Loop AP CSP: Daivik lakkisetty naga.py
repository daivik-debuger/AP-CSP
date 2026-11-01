# Name: Daivik lakkisetty naga
# AP CSP - Cookie Sales Loops Assignment

# lists for the student names and the boxes they sold
students = ["John", "Sophie", "Liam", "Zoe", "Caleb"]
cookie_boxes = [8, 15, 12, 6, 20]

# 1. Total Sales
# add up all the boxes using sum()
total_sales = sum(cookie_boxes)
print("Total cookie boxes sold:", total_sales)

# 2. Top Sellers
# loop through the list and print anyone who sold over 10
print("\nTop Sellers:")
for i in range(len(students)):
    if cookie_boxes[i] > 10:
        print(students[i])

# 3. Under Goal
# loop through and print anyone who sold less than 10, plus their count
print("\nStudents Below Goal:")
for i in range(len(students)):
    if cookie_boxes[i] < 10:
        print(students[i], "-", cookie_boxes[i], "boxes")

# 4. Search for a student
# ask user for a name to look up
search_name = input("\nEnter a student's name: ").strip()

# flag variable to see if we found the student
found = False

# loop through to check each name
# .lower() makes it so capitals/lowercase don't matter
for i in range(len(students)):
    if students[i].lower() == search_name.lower():
        print(students[i], "sold", cookie_boxes[i], "boxes.")
        found = True
        break  # stop looping once found

# if we checked everyone and didn't find a match
if not found:
    print("Student not found")
    