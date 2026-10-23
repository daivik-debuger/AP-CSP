# Name: Daivik Lakkisetty Naga
# Assignment: 2. Username Generator
# Course: AP CSP


names = ["Jennifer", "Michael", "Tyler", "Sophia", "Brandon"]
years = [2027, 2028, 2027, 2029, 2028]


usernames = []
emails = []
accounts = []

# Loop through each student to create accounts
for i in range(len(names)):
    # 1. String slicing:
    # - name_slice: full name slice names[i][:] (or use names[i][:4] for first 4 letters)
    # - year_slice: last 2 digits of graduation year using string slicing str(years[i])[2:]
    name_slice = names[i][:]
    year_slice = str(years[i])[2:]
    
    # 2. Combine and convert to lowercase
    username = (name_slice + year_slice).lower()
    usernames.append(username)
    
    # 3. Create email address
    email = username + "@school.edu"
    emails.append(email)
    
    # 4. Generate final account entry (as a formatted dictionary or string)
    account_info = {
        "Name": names[i],
        "Year": years[i],
        "Username": username,
        "Email": email
    }
    accounts.append(account_info)

# 5. Identify the longest username
longest_username = usernames[0]
for user in usernames:
    if len(user) > len(longest_username):
        longest_username = user

# Display the Results
print("==================================================")
print("             STUDENT ACCOUNT LIST                 ")
print("==================================================")
for acc in accounts:
    print(f"Name: {acc['Name']:<10} | Username: {acc['Username']:<12} | Email: {acc['Email']}")

print("==================================================")
print(f"Longest Username: '{longest_username}' ({len(longest_username)} characters)")
print("==================================================")
