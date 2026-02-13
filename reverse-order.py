#input number greater than 1
n = int(input("Enter the value of n: "))

# print the number from n to 1
print("number from {0} to {1} are: ".format(n,1))

#loop to print number for ( i<0;i<n;i++)  for (i=n; i>=0;i--)
for i in range(n,0,-1):
    print(i)