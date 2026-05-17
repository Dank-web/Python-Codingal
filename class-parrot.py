#create class
class Parrot:
    #class attribute
    species = "bird"
    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

#acces the class attributes
print("Blu is a", blu.species)
print("Woo is also a", woo.species)

# access the instance attributes
print(blu.name, "is", blu.age, "years old")
print(woo.name, "is", woo.age, "years old")