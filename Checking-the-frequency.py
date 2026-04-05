#Initialize dictionary
test_dict = {"Codingal": 2, "is" : 1, "best" : 2, "for" : 2, "Codingal" : 1}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

#Initislise
k = 1

#using loop
#select key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

#printing result
print("Frequency of K is : " + str(res))
