# list = [1.2.3.4.5,6,2,3,5,1]
# 뭐는 짝수입니다.
# 뭐는 홀수입니다.

list1 = [1,2,3,4,5,6,2,3,5,1]
# re = 0
# for i in list:
#     if i =="c" :
#         break
#     print(i)
# if(list[re] % 2==0):
#     print("짝수입니다")
# else:
#     print("홀수입니다")

# for el in list1:
#     if el % 2 ==0:
#         print(f"{el} 은 짝수 입니다")
#         elif el % 2==1:
#         print(f"el은 홀수입니다")
i = 0
while i<len(list1):
    
    if list1[i] % 2 == 0:
        print(f"{list1[i]}은 짝수입니다")
    elif list1[i] % 2==1:
        print(i)
        # print(f"{list1[i]} 은 홀수 입니다")
        continue # 반복문의 continue 뒤 실행 x
        # break 반복문이 끝남
    i+=1   
    # print(f"--------{list[i]}---------")


list1 = [1,2,3,4,5,6,2,3,5,1]
for el in list1:
    match el % 2:
        case 1:
            print(f"{el}은 홀수 입니다")
        case 0:
            print(f"{el} 은 짝수 입니다")
    # if el % 2 ==0:
    #     print(f"{el} 은 짝수 입니다")
    # elif el % 2==1:
    #     print(f"{el} 은 홀수입니다")


# (람다) 버전 3.6부터 지원
# 예제) list1 의 요소를 *2 해서 찍어봐라

        