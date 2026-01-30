#assigning different variables
name = "Penguin"
age = 15
is_student = True
weight = 38.5

#printing different variables and their data types
print("Name:", name)
print("Data Type of Name is", type(name))

print("age:", age)
print("Data Type of age is", type(age))

print("IS Student:", is_student)
print("Data Type of weight is", type(is_student))

print("Weight", weight)
print("Data Type of weight is", type(weight))

#Type casting to convert the datatype of variables
print("\n after Type Casting....")
age = str(age)#type casting
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of age is", type(age))
