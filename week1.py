# 변수 1번
Korean = 50
Math = 80
English = 30
print((Korean + Math + English) / 3)

# 변수 2번
score = 409298570
if(score % 2 == 0):
    print("짝수입니다.")

# 변수 3번
subject = '국어:수학:영어:프로그래밍'
print(subject.replace(':',', '))

# 변수 4번
list = [1, 70, 3, 80, 5]
list.reverse()
print(list)

# 변수 5번
list = ["파이썬은", "정말", "편하다"]
print(list[0], list[1], list[2])

# 변수 6번
list = [1, 50, 410, 10, 3, 4, 5]
list.sort()
print(list)

# 변수 7번
love = " I love python "
print(love.strip())

# 제어문 1번
a = 0
for i in range(1,101):
    a = a + i
print(a)

# 제어문 2번
a = 0
sum = 0
while a < 101:
    sum += a
    a += 1
print(sum)

# 제어문 3번
a = 0
sum = 0
while a <= 100:
    if a % 3 == 0:
        sum += a
    a += 1
print(sum)

# 제어문 4번
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for i in score:
    total += i
average = total / 10
print(average)

# 제어문 5번
list = [1, 3, 5, 40, 90, 100, 2020]
a = []
for i in list:
    if i % 2 == 1:
        a.append(i*2)
print(a)
        

# 제어문 6번
for i in range(5):
    for j in range(i+1):
        print('*', end="")
    print('')