num1, num2 = input().split()

num1 = int(num1[2] + num1[1] + num1[0])
num2 = int(num2[2] + num2[1] + num2[0])
print(max(num1, num2))