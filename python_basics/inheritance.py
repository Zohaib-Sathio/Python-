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



# Another child class
class Dog(Animal):
    def __init__(self, name, isTamed, breed):
        self.breed = breed
        super().__init__(name, isTamed)

    def full_info(self):
        print(f'Name of the animal is {self.name}')
        print(f'Is animal tamed? : {self.tamed}')
        print(f'Breed of the dog is: {self.breed}')
    

dog = Dog('Wasay :)', False, 'Bull Dog')
dog.display()
dog.full_info()