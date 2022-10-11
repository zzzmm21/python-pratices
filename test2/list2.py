# i = 2
# sum =0
# while i < =20:
#     
#     if i % 2== 0:
#         sum= sum+i ============ sum+= i 
#         i= i+1      
# # print(sum)

# e= 0
# for el in range(2,21,2):
#     e += el
# print(e)
        
        
        
# print(sum)

# i = 0

# for el in list1:
#     i +=  el
# if i % 2==0:
#     print(sum*2



    #    2부터 30 까지 소수 (1과 자신) 리스트 뽑아내기
    # [2,3,5,7,11,13,17,19,23,29]
# list1 = []
# for i in range(2,31):
#     a= True # 소수인가?
#     #  i=3, 2<= j <3
#     for j in range(2,i):
#         if i%j == 0:
#             a= False
#             break
#     if a:
#         list1.append(i)
# print(list1)





# num = 2
# for i in range(2,10):
#     for num in range(1,10):
#         print(f"{i} * {num}={num*1}")



# text = "*"
# for  i in range(1,6):
#     st = ""
#     for  j in range(1,i):
#         st = text* j
#     print(st)


#  파이선은 절차 지향 언어
#  자바 OPP
# 함수
# define 정의
#  sum(a,b)
#  return 반환
#  sum(a,b) => a,b 매개 변수
#  isPrimary Key= true cammel case
#  is_primary_key = True snake case
from ast import arg
from re import I


# def sum(a,b):
#      return a+b

# print(sum(1,2)) # sum(1,2) => 1,2 => 인수

# #  arg = argument = 매개 변수
# def sum1(*args):
#     pppp= 0
#     for  arg in args:
#         pppp+= arg
#     return pppp
# print(sum1(1,1,1,1,1,1,1))

# def printfunc(**kwarg):
#     print(kwarg)
# printfunc(a= 1)

# def makehuman(name,age):
#     return{"name":name,"age":age}
# human1 = makehuman("kim",30)
# human2 = makehuman("kim",40)
# print(human1)
# print(human2)


# def isPrimaryNumber(num):
#     isPrimary= True
#     for j in range(2,num):
#         if num%j == 0:
#             isPrimary= False
#             break
#     if isPrimaryNumber:
#         return f"{num}은 소수 입니다"
#     else:
#         return f"{num}은 소수가 아닙니다"
# print(isPrimaryNumber(5))


# def isPrimaryNumbers(*nums):
#    for num in nums:
#         isPrimary =True
#         for j in range(2,num):
#             if num%j == 0:
#                 isPrimary = False
#                 break
#         if isPrimary:
#             print(f"{num}은 소수 입니다")
#         else:
#             print(f"{num}은 소수가 아닙니다")
# isPrimaryNumbers(9,5,4,3)




name = "park" # 전역 변수
name1 = "lee" #전역 변수

def setname1(name): # 매개변수
    print(f"2.{name}") #kim
    
    name = name ## 지역변수

    print(f"3.{name}{name1}") #kim lee



print(f"1.name1:{name1}") # 1.name 1:
print(f"1.{name}") #park
setname1("kim") #인자값 인수
print(f"4.{name}") #park
print(f"2.name1:{name1}")#2.name1: 

#코딩 테스트 1.백준(난이도가 좀더 잇음) , 프로그래머스



