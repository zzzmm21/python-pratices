# 제어문
a = 2
b = 5
if  a> b:
    print(f"{a} 는 {b}보다 크다")
    print("2")
    print("3")
elif a < b:
    print(f"{a}는 {b}보다 작다")
else: # 위조건이 아니면 다 아니면 마지막
    print("else")


x= {"company":"카카오","is part time":True}
# or 또는 카카오또는 네이버
# and는 카카오 이면서 네이버이다
if x.get("company") == "카카오":
    if x.get("is part time"):
        print("비정규직")
    else:
        print("대기업 정규직원")

    print("대기업 직원이시네요")
elif x.get("company") == "네이버" :
    print("대기업 직원이시네요")

else:
    print("중견기업 직원이시네요")



# # match x.get("company"):
#     case"카카오":
#         print("대기업")
#     case"네이버":
#         print("대기업")
#     case _:
#          print("중견기업 직원이시네요")






