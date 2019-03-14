user_num1 = int(input("Please enter first number: "))
user_num2 = int(input("Please second number: "))
user_num3 = int(input("Please enter third number: "))
user_num4 = int(input("Please enter four number: "))
user_num5 = int(input("Please enter fifth number: "))

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





