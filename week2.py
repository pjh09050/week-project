# 1번
score = int(input("input : "))
if score >= 80:
    grade = "A"
elif score >= 50:
    grade = "B"
elif score >= 30:
    grade = "C"
else:
    grade = "F"
print("output : ", grade)

# 2번
TF = int(input("input : "))
if TF % 2 == 0:
    result = True
else:
    result = False
print("return : ", result)

# 3번
number = (input("input : "))
year = number[0:2]
sex = number[7]
if sex == "1" or sex == "3":
    sex = '남자'
elif sex == "2" or sex == "4":
    sex = '여자'
else:
    sex = '중성'
print("output : ", year+"년생,", sex)

# 4번
number1 = int(input("input : "))
plus = input()
number2 = int(input())
result = 0
if plus == "+":
    result = number1 + number2
elif plus == "-":
    result = number1 - number2
elif plus == "*":
    result = number1 * number2
elif plus == "/":
    result = number1 / number2
print("output : ", result)

#5번
money = int(input("input : "))
one = money // 5000
two = (money % 5000) // 1000
three = ((money % 5000) % 1000) // 500
four = (((money % 5000) % 1000) % 500) // 100
five = ((((money % 5000) % 1000) % 500) % 100) // 50
six = (((((money % 5000) % 1000) % 500) % 100) % 50)// 10
print("output : ", "5000원 : ", one, "개", "\n1000원 : ", two, "개",
"\n500원 : ", three, "개", "\n100원 : ", four, "개", "\n50원 : ", five, "개", "\n10원 : ", six, "개")

# 6번
import math
# ax^2+bx+c
a = int(input("input : "))
b = int(input("input : "))
c = int(input("input : "))
x1 = ((-b - (math.sqrt(math.pow(b,2) - 4 * a * c))) / 2 * a)
x2 = ((-b + (math.sqrt(math.pow(b,2) - 4 * a * c))) / 2 * a)
print("x1 =", x1, ", x2 =", x2)