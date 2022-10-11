# 파이썬 무슨 언어인가?
# 절차지향
# type 숫자 int ,문자 str,
#  list, set , tuple, dict
#  a=1
#  a= "stt" 
#  a= []
#  a= {}
#  a = ()
#  a = {key:value}

# 동적 타이핑
# 장점 : 타입을 지정 안해도 괜찮
# 단점 : 오류 발생 가능

# 스크립트 언어
# 소스 코드를 한줄씩 읽어서 곧바로 실행
# python 문법으로 코드를 작성했는데
# 컴퓨터 언어는 0110
# 컴파일 python -> 컴퓨터 언어
# 따로 컴퓨터 언어로 바꿔서 따로 파일을 만들어서 그것을 실행


#  플랫폼 독립적: os 상관없다(window , mac, linux)

# 제어문
#  if , elif ,else 
#  match case 


# 반복문
# for in :
#  break continue
#  while
#  람다 lamda (map,reduce,filter)

from functools import reduce


list1 = [9,1,2,4,3]
def sum(x,y):
    print(f"{x}{y}") #format
    return x+y
a = reduce(lambda x,y : sum(x,y),list1)


# 함수
# def :
# def sum(a,b) :매개 변수
#  return a+b
# sum(1,2) 1,2 인수
# 
#  def sum(*a) *a tuple
#  sum = (1,2,3,4)
#  def sum(**a) :*a dict
#  sum(name= kim , age =11)
user = {"id" :"id","pass":"pass","name":""}
names = ["kim","lee","park"]
namelist=list(map(lambda x: {"id":"id", "pass":"pass","name":x},names))
print(namelist)


# name = "kim" 전역변수
#  def printname(name):
    # name = "lee" 지역변수

# 파일 입출력
# f= open(파일,mode,)
# encording UTP-8

# 입력받고 싶을떄 : input


# class
# 왜 씀? 반복작업 중복되는것을 한번에 처리하려고
# 객체 지향
# class name(상속):
#   def __init__:
# 상속 접글 할때 super()
# def__init(self):
# self 자신

# improt 뭔가 이파일말고 다른곳에서 불러올때
# 


# 정규식 개념 serach match
# park@gmail.com
# 이거 이메일 형식 맞음?
# import re
# import random


# C:\test - > C:\test\test2
# 상대경로
# ./test2
# .. 상위폴더
# 절대경로
# C:\test\test2

# 1 자연수 뒤집어 배열로 만들기
# 2 제일 작은수 제거하기 
# 3 두정수 사이의 합
# 4 정수 제곱근 판별

