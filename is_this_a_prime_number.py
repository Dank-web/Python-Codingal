#take two input from user
lower = int(input("enter a lower range: "))#0
upper = int(input("enter a upper range: "))#5

print("Prime number between", lower, "and", upper, "are:")#num=0
#iterate loop from lower limit to upper limit
for num in range(lower , upper + 1):
    #all prime number are greater then 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)