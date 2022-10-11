# list1 의 전체합
from functools import reduce


list1 = [1,2,3,4,5,6,2,3,5,1]
sum = 0 
for el in list1:
    sum +=  el
print(sum)

sum2=reduce(lambda x,y : x+y,list1 )
# 합계 구할떄
print(sum2)
