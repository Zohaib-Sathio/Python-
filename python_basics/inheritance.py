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

class Age():
    def __init__(self, age):
        self.age = age
    
    def show_age(self):
        print(f'Age is : {self.age}')
        
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


class LivingThing(Age, Animal):
    def __init__(self, name, isTamed, age):
        Animal.__init__(self, name, isTamed)
        Age.__init__(self, age)
    
    def show_info_living_thing(self):
        print('Child Class Method')


species = LivingThing('Bunty', True, 10)
species.display()
species.show_age()
species.show_info_living_thing()