# Basic concept
list = [23, 43, 234, 402]
try:
    for i in range(5):
        print(list[i])
except:
    print("An error occurred \nIndex out of bounds")

#Defining multiple exceptions

def fun(num):
    if num < 10:
        new_num = num / (num - 2)
        print('new_num has been created')
    print(f'Value of new number is {new_num}')


try:
    fun(4)
    fun(7)
    # fun(2)
    fun(15)
except ZeroDivisionError:
    print('Cannot divide the number with 0')
except NameError:
    print('Could not find the variable')