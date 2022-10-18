# Parent Class
class Animal():
    def __init__(self, name, isTamed):
        self.name = name
        self.tamed = isTamed
    
    def display(self):
        print(f'Name of the animal is {self.name}')
        print(f'Is animal tamed? : {self.tamed}')
    
animal = Animal('Bully', True)
animal.display()
        
# Child Class
class Cat(Animal):
    def sound(self):
        print('Sound of the cat is Meowww!')


cat = Cat('Lazi', True)
cat.sound()