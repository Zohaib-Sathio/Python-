# basic usage
i = 0
while i < 5:
    print(i)
    i = i + 1

# usage with list as stack
print("Usage with list as stack")
a = ['a', 'b', 'c', 'd']
while a:
    print(a.pop())


# Single statement while block

count  = 0
while count < 3 : count += 1; print(count)


# while loop with else

nums = [3, 6, 343, 42, 115]
while nums:
    print(nums.pop())
else:
    print("No break keyword found")


# while loop with user input

entered_num = int(input("Enter 1 to exit loop? "))
while entered_num != 1:
    entered_num = int(input("Ente 1 to exit loop? "))
else:
    print("yeahh ! you exited the while loop")
