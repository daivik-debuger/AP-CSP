#Name: Daivik Lakkisetty Naga
#Date:10/26/2026
#Period: 1st

names = ["anderson", "jhonson", "garcia", "brown", "williams", "banks", "verstapen"]

labels = []

for name in names:
    clean_name = name.lower()
    first_three = clean_name[:3]               
    total_length = len(clean_name)             
    label = first_three + str(total_length)     
    labels.append(label)                        

print(labels)
