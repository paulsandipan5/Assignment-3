# Write a Python function to sum all the numbers in a list(inputs available)

def sum(num):
    sum = 0
    for i in lt:
        sum+=i
    return sum
lt = []
num = int(input("Enter the number of elements:"))
for j in range(num):
    lt.append(int(input()))
print("The sum is",sum((lt)))

