class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color
    def bark(self):
            return "Woof!"
    def dog_type(self):
            return "Lovely Pet!!!"

dog1 = Dog("Brown", "TP", "Black")
dog2 = Dog("Sweetu", "TP", "Brown")


print(dog1.dog_type())
print(dog2.bark())
print(dog1.color)





