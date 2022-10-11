from functools import reduce


list1 =[1,2,3,4,5,6,2,3,5,1]
list2 =[]
for el in list1 :
    if el >= 4:
        list2.append(el)

print(list2)


list01= list(filter(lambda x: x >=4 , list1))
print(list01)