# 여러가지 모듈
import calendar
import math
import random
import re
import webbrowser

# print(math.pi)
# calendar.prmonth(2022,10)
# webbrowser.open("https://naver.com")
# print(random.random())
# 정규식
# reg=re.compile("[0-9]{4.5}")
# id = "2ㅁㅁㅁㅁ2455"
# id2 = "24455"
# print(reg.match(id))
# print(reg.search(id))


# 회원가입
#  비밀번호에서 특수 문자, 영어 대문자 포함
#  AI 자연어 처리
#  나는 오늘 좋다.
#  이메일 park@gmail.com

# reg = re.compile("([A-za-z0-9]+@[A-za-z0-9]+\.[A-za-z]{2,3})")
# print(reg.match("park@gmail.com"))

#  check 정규식
#  로또 1 ~45 중복없이 6자리
# random
# numbers= []
# for i in range(0,6):
#     num = int(random.random()*45+1)
#     print(int(num))
# lotto = []
# for i in range(0,5):
#     numbers = []
#     while len(numbers)<6:
#         num = int(random.random()*45+1)
#         tmpNumber = numbers.copy()
#         tmpNumber.append(num)
#         setNumbers =set(numbers.copy())
#         if len(setNumbers) == len(tmpNumber):
#             numbers.append(num)
#     lotto.append(numbers)
# for text in lotto:
#     print(text)

reg = re.compile("([0-9]{3,4}-[0-9]{4,5}-[0-9]{4})")
phone_number = "010-2222-3333"
print(reg.match(phone_number))

def average(num_list):
    answer = 0
    for i in num_list:
        answer += i

    return answer / len(num_list)
# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [4,3,2] 
print("평균값 : {}".format(average(list)));