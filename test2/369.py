


# def gama(cur, myInput):       
#     answer = str(cur)
#     for c in str(cur):
#         if c== "3" or  c=="6" or c=="9":
#             answer = "c"
#     if myInput == answer:
#         print("맞았따")
#         return True
#     else:
#         print("gmae over")
#         return False


# i  = 0
# while True:
#     i += 1
#     myInput = input(f"369369 현재 {i} ")
#     iswin = gama(i,myInput)
#     if(not iswin):
#         break
# def s(phone_num):
#     answer= ""
#     for i in range(0,len(phone_num)):
#         if i < len(phone_num) - 4:
#             if phone_num[i] =="-":
#                 answer += "-"
#             else:
#                 answer +="*"
#         else :
#             answer += phone_num[i]
#     return answer
# phone_num = input("번호 000-0000-0000")
# print(s(phone_num))


print("test1")
print("test1")


print("test1")
# 약수의합
def solution(n):
    sum=0
    answer=0
    for i in range(1,n+1):
        if n% i ==0: 
           sum +=i
           answer = sum
    return answer
print(solution(12))
# 자리수 더하기
def solution(n):
    N=[int(i) for i in str(n)]

    return sum(N)
print(solution(12))
# 위아래 같은거
# 
def solution(n):
    sum= str(n)
    add = 0
    for i in range(len(sum)):
        add += int(sum[i])
    return add
print(solution(12))

