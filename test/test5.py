#제어문
a = 10
b = 5
#print(f" a > b {a>b} = true 크다 false 작다" )

str1 = ""
if a> b : 
# 조건이 true 면 아래문장을 실행한다
    str1 = "크다"
   
elif a< b: 
    #elif 위의 조건이 아니면*(false) 이걸실행
    str1 = "작다"
    

else: 
    # else if도 false elif false 다아니면 실행
    str1 ="같다"
print(f"a >  b {str1}")



c = [1,2,3,4,5]
if len(c) > 3:
    print(c[0])
#
#

if len(c) <=  3:
    print(c[0])