print("welcom to the ")
# Name: Daivik Lakkisetty Naga
# Date: 10/27/2026
# Period: 1st

# Given lists
Names = ["John", "Paul", "Sophie", "Ringo", "Francis", "Liam", "Zoe", "Caleb", "Myah", "Haper"]
Sizes = ["large", "small", "large", "small", "large", "large", "small", "large", "small", "large"]

# Lists to store the names for each size
small_names = []
large_names = []

# Loop through the lists and separate names based on size
for i in range(len(Sizes)):
    if Sizes[i] == "small":
        small_names.append(Names[i])
    elif Sizes[i] == "large":
        large_names.append(Names[i])

# Calculate the totals
small_total = len(small_names)
large_total = len(large_names)

# Keep prompting the user (matches the screenshot)
while True:
    choice = input("Would you like to see Large or Small totals? (L or S)").upper()
    
    if choice == "S":
        print(small_names)
        print(small_total)
    elif choice == "L":
        print(large_names)
        print(large_total)
