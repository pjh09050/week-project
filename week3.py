# 1번
import random
lotto = []
while len(lotto) < 6:
    random_number = random.randint(1,45)
    if random_number not in lotto:
        lotto.append(random_number)
lotto.sort()
print("output :\n", lotto)

# 2번
a = str(input("input : "))
print("output: ")
print("문자의 개수 : ", len(a))
print("가장 큰 문자열 : ", max(a))
print("뒤집은 문자열 :", ''.join(reversed(a)))

# 3번
import datetime
now = datetime.datetime.now()
after = datetime.datetime.now() + datetime.timedelta(days = 49, hours = 1, minutes = 8, seconds = 7)
print("현재 : ",now.year,"년",now.month,"월",now.day,"일",now.hour,"시",now.minute,"분",now.second,"초")
print("미래 : ",after.year,"년",after.month,"월",after.day,"일",after.hour,"시",after.minute,"분",after.second,"초")

# 4번
import re
text = input("input: \n")
email = re.compile( '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$').finditer(text)
for i in email: 
	print("올바른 형식입니다.")

# 5번
dic = {'apple' : '사과', 'banana' : '바나나', 'camel' : '낙타'}
while True:
    print("output: \n메뉴를 선택해주세요.\n1. 입력\n2. 전체출력\n3. 영어로검색\n4. 한글로검색\n5. 종료\n")
    menu = input('input: \n')
    print('')
    if menu == '입력':
        print('output: \n'+menu+'를 선택하셨습니다.')
        print('영단어:한글단어 쌍으로 입력해주시고, 끝났다면 나가기를 입력해주세요.\n')
        print("input : ")
        while True:
            out = input()
            if out == '나가기':
                print('')
                break
    elif menu == '전체출력':
        print('output :\n'+menu+'결과입니다.')
        print(dic)
        print("")
        while True:
            print("input : ")
            full = input()
            print("")
            if full == '전체출력':
                print('output :\n'+menu+'결과입니다.')
                print(dic)
                print("")
            elif full == '나가기':
                break
    elif menu == '영어로검색':
        print('output :\n'+menu+'을 선택하셨습니다.')
        print("영단어를 입력하세요.\n")
        while True:
            english = input('input : \n')
            print('')
            if english in dic.keys():
                print('output :\n'+dic[english])
                print('계속 검색 가능합니다.')
                print('나가시려면 나가기를 입력해주세요\n')
            elif english == '나가기':
                break
    elif menu == '한글로검색':
        print('output :\n'+menu+'을 선택하셨습니다.')
        print("한글를 입력하세요.\n")
        while True:
            korean = input('input : \n')
            print('')
            if korean in dic.values():
                for key, value in dic.items():
                    if value == korean:
                        print('output :\n'+key)
                        print('계속 검색 가능합니다.')
                        print('나가시려면 나가기를 입력해주세요\n')
            elif korean == '나가기':
                break
    elif menu == '종료':
        break