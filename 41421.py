# # def rm_small(mylist):

# #     index = 0
# #     num = mylist[0]
# #     for i in range(len(mylist)):


# #         if num <= mylist[i]:
# #             num = num
# #         else:
# #             num = mylist[i]
# #             index = i

# #     return mylist[:index]+mylist[index+1:]

# # my_list = [5,3,2,1]
# # print(format(rm_small(my_list)))


# # 정수 합
# from re import A


# def solution(a, b):
#     answer = 0
#     if a == b:
#         return a
#     elif a > b:
#         for i in range (b, a+1):
#             answer += i
#     else:
#         for i in range(a, b+1):
#             answer += i
    
#     return answer
# print(solution(4,4))

# # 자연수 뒤집어 배열

# def solution(n):
#     answer = []
#     for i in str(n)[::-1]:
#         answer.append(int(i))
#     return answer
# print(solution(12345))

# def solution(n):
#     answer = 0
#     nub = n**0.5
#     if nub == int(nub):
#         answer = (nub+1)**2
#     else:
#         answer = -1
#     return answer
# print(solution(121))


# def solution(a,b):
#     answer = 0
#     if a== b:
#         return a
#     elif a>b:
#         for i in range(b,a+1):
#             answer +=i
#     else:
#         for i in range(a,b+1):
#             answer +=i
#     return answer
# print(solution(4,4))



# def solution(n):
#     answer=0
#     nub = n**0.5
#     if nub == int(nub):
#         answer = (nub+1)**2
#     else:
#         answer = -1
#     return answer
# print(solution(121))


# def solution(a,b):
#     answer = 0 
#     if a == b :
#         return a
#     elif a>b:
#         for i in range(b,a+1):
#             answer += i
#     else :
#         for i in range(a,b+1):
#             answer +=  i
#     return answer


# def solution(n):
#     answer=0 
#     nub = n**0.5
#     if int(nub) == nub:
#         answer =int(nub+1)**2
#     else:
#         answer = -1
#     return answer
# print(solution(121))


# def solution(n):
#     answer = []
#     for i in str(n)[::-1]:
#         answer.append(int(i))
#     return answer
# print(solution(12345))



# def solution(arr):
#     answer = []
#     if len(arr)==1 :
#         return [-1]
#     minNmber =100000
#     for a in arr:
#         if a <minNmber:
#             minNumber = a
#     # 제거하기
#     arr.remove(minNmber)
#     for a in arr:
#         if minNumber != a:
#             answer.append(a)
#     return answer


# def solution(n):
#     answer=[]
#     for i in str(n)[::-1]:
#         answer.append(int(i))
#     return answer
# print(solution(2344))

# def solution(n):
#     answer=0
#     num = n**0.5
#     if num==int(num):
#         answer=int(num+1)**2
#     else:
#         answer= -1
#     return answer
# print(solution(16))



# def solution(n):
#     answer= 0
#     num=n**0.5
#     if num == int(num):
#         answer= int(n+1)**2
#     else:
#         answer =-1
#     return answer


# def solution(n):
#     answer=0
#     for i  in range(1,n):
#         if i*i ==n:
#             answer = i
#     if answer==0:
#         return -1
#     return(answer+1)*(answer+1)

from re import S




    # minnumber=1500
    # if minnumber> n:

    # return answer