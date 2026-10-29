# Name: Daivik lakkisetty naga

students = ["John", "Sophie", "Liam", "Zoe", "Caleb"]
cookie_boxes = [8, 15, 12, 6, 20]


total_sales = sum(cookie_boxes)
print("Total cookie boxes sold:", total_sales)


print("\nTop Sellers:")
for i in range(len(students)):
    if cookie_boxes[i] > 10:
        print(students[i])

print("\nStudents Below Goal:")
for i in range(len(students)):
    if cookie_boxes[i] < 10:
        print(students[i], "-", cookie_boxes[i], "boxes")


search_name = input("\nEnter a student's name: ")

if search_name in students:
    index = students.index(search_name)
    print(search_name, "sold", cookie_boxes[index], "boxes.")
else:
    print("Student not found")


