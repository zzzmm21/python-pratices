list1 =["안","녕","하","세","요"]
index = 0 
hi =""
while index < len(list1):
    print(list1[index])
    hi +=list1[index] 
    index += 1
print(hi)

# while 조건이 true인 동안 아래를 실행함:
for i in range(0,len(list1),4):
    hi += list1[i]
print(hi)
for element in list1:
    hi = hi+ element
print(hi)

# b= 2+4+6+8+10+12+14+16+18+20
# print(b)
