# 1번
score = int(input("input : "))
if score > 100 or score < 0:
    grade = "범위를 잘 입력하세요."
elif score >= 80:
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
        if number2 == 0:
            print("분모는 0을 사용할 수 없습니다.")
        else:
            result = number1 / number2
elif plus == "%":
    result = number1 % number2
print("output : ", result)

#5번
list = [0 for i in range(6)] 
money = int(input("input : "))
while money != 0:
    if money >= 5000:
        list[0] += 1
        money = money - 5000
    elif money >= 1000:
        list[1] += 1
        money = money - 1000
    elif money >= 500:
        list[2] += 1
        money = money - 500
    elif money >= 100:
        list[3] += 1
        money = money - 100
    elif money >= 50:
        list[4] += 1
        money = money - 50
    elif money >= 10:
        list[5] += 1
        money = money - 10
print("output : 5000원 : ",list[0],"개")
print("1000원 : ",list[1],"개")
print("500원 : ",list[2],"개") 
print("100원 : ",list[3],"개")
print("50원 : ",list[4],"개")
print("10원 : ",list[5],"개")

#6
import math
a = float(input("input : "))
b = float(input("input : "))
c = float(input("input : "))
D = (b**2) - (4*a*c)
if D>0:
    x1 = ((-b - (math.sqrt(math.pow(b,2) - 4 * a * c))) / 2 * a)
    x2 = ((-b + (math.sqrt(math.pow(b,2) - 4 * a * c))) / 2 * a)
    print("output :", "x1 =", x1, ", x2 =", x2)
elif D==0:
    x = -b / 2*a
    print("output :", "x =", x)
else:
    print("output : 허근입니다. ")
