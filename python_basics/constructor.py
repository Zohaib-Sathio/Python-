#Basic Usage
class MyHobby:
    def __init__(self):
        self.hobby_name = "Rubik's Cube"
        self.sd = 'asffsf'
    
    def print_hobby(self):
        print(self.hobby_name)


obj = MyHobby()
obj.print_hobby()


#Adding two numbers
#Parametrized constructor
class Addition:
    first_num = second_num = result = 0
    def __init__(self, f, s):
        self.first_num = f
        self.second_num = s
    
    def display(self):
        print("First number = " + str(self.first_num))
        print(f'Second number = {self.second_num}')
        print("Addition of two numbers = " + str(self.result))

    def calculate(self):
        self.result = self.first_num + self.second_num

    
obj2 = Addition(120 ,420)
obj2.calculate()
obj2.display()