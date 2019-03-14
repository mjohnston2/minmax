user_num1 = int(input("Please enter first number between 0-10000: "))

while user_num1 > 10000 or user_num1 <0:
    print("Invalid Number")
    user_num1 = int(input("Please enter first number between 0-10000: "))
    
user_num2 = int(input("Please second number : "))

while user_num2 > 10000 or user_num2 <0:
    print("Invalid Number")
    user_num2 = int(input("Please enter first number between 0-10000: "))

user_num3 = int(input("Please enter third number between 0-10000: "))

while user_num3 > 10000 or user_num3 <0:
    print("Invalid Number")
    user_num3 = int(input("Please enter first number between 0-10000: "))

user_num4 = int(input("Please enter four number between 0-10000: "))

while user_num4 > 10000 or user_num4 <0:
    print("Invalid Number")
    user_num4 = int(input("Please enter first number between 0-10000: "))

user_num5 = int(input("Please enter fifth number between 0-10000: "))

while user_num5 > 10000 or user_num5 <0:
    print("Invalid Number")
    user_num5 = int(input("Please enter first number between 0-10000: "))




max = user_num1

if user_num2 > max:
    max = user_num2

if user_num3 > max:
    max = user_num3
if user_num4 > max:
    max = user_num4
if user_num5 > max:
    max = user_num5
print(max)

min = user_num2

if user_num1 < min:
    min = user_num1
if user_num3 < min:
    min = user_num3
if user_num4 < min:
    min = user_num4
if user_num5 < min:
    min = user_num5
print(min)





