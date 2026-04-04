#Create a tuple with different data types
tuplex = ("tuple", False, 3.2,1)
print(tuplex)
#Create a tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
#Tuples are immutable, so you can not add new elements
#using merge of tuples with the + operetor you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
#Counts the number of occurrences of item 50 from a tuple 
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))
#Create a tuple
tuplex = (2, 4, 3, 5, 6, 7, 8, 6, 1)
#used tuples[start:stop] the start index is incursive and the stop index
_slice = tuplex(3:5)
#is exclusive
print(_slice)
#if the start isn't defined, is taken from the beginning of the tuple
_slice = tuplex[:6]
print(_slice)