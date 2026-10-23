
names = ["Jennifer", "Michael", "Tyler", "Sophia", "Brandon"]
years = [2027, 2028, 2027, 2029, 2028]

usernames = []
emails = []
account_list = []


for i in range(len(names)):
    
    name_slice = names[i][:]
    year_slice = str(years[i])[2:]
    
    
    username = (name_slice + year_slice).lower()
    usernames.append(username)
    
    
    email = username + "@school.edu"
    emails.append(email)
    
    
    account_list.append(f"Name: {names[i]:<10} | Username: {username:<12} | Email: {email}")


longest_username = usernames[0]
for user in usernames:
    if len(user) > len(longest_username):
        longest_username = user


print("--- Final Account List ---")
for account in account_list:
    print(account)

print(f"\nLongest Username: {longest_username} ({len(longest_username)} characters)")
