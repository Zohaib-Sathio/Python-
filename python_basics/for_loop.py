
# basic iteration
for i in range(10):
    print(i)

# iterating list using for loop
print("iterating list")
list = [1, 3, 6, 8, 9]
for item in list:
    print(item)

# iterating the dictionary
print("Iterating the dictionary")
d = dict()
d["Name"] = "Zohaib"
d["Surname"] = "Sathio"
for i in d:
    print(f'{i}:  {d[i]}')

# Iterating the String 
print("iterating the String")
name = 'ZohaibHussain'
for char in name:
    print(char)

# for-else loop
print("Demonstrating for-else loop")
for num in [2,5,7,8]:
    # if loop is ended because break keyword then else code is not executed
    # if num == 5:
    #     break
    print(num)
else:
    print("No break/n")
