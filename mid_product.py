num = input("Enter a number: ")

length = len(num)

if length % 2 == 1:
    # Odd number of digits
    middle = int(num[length // 2])
    product = middle
else:
    # Even number of digits
    mid1 = int(num[length // 2 - 1])
    mid2 = int(num[length // 2])
    product = mid1 * mid2

print("Product of middle digit(s):", product)