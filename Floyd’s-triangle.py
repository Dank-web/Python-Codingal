#take input from user
rows = int(input("please enter the total number of rows   :  "))
number = 1 #initialise by 1

print("Floyds Trinange")
#outer loop for number of rows
for i in range(1, rows + 1):# 1 2 3 4 5
    #inner loop for number of columns
    for j in range(1, i + 1):   # 1 2 3 4 5
        #display result
        print(number, end = "   ")
        number = number + 1
    print()