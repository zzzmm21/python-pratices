list1 = [1,2,3,4,5,6,2,3,5,1]
list2 = []
for el in list1:
    list2.append(el * 2)
print(list2)

list3 =[]
for a in range(0,len(list1)):

    list3.append(list1[a] *2 )
print(list3)

# map 은 새로운 리스트를 만든다 (반환한다)
list4 = list(map(lambda el : el*2,list1))
print(list4)

tmpd = {"name": "kim","age":100}
list5 = [tmpd,tmpd,tmpd]
list6 = list(map(lambda el: el.copy(),list5)) 
#[tmpd.copy(),tmpd.copy(),tmpd.copy()]
list7 = list5.copy() #list5 = [tmpd,tmpd,tmpd]
print(list5)
print(list6)
print(list7)
list5.append(1)
print(list5)
print(list6)
print(list7)
tmpd["age"] = 10
print(list5)
print(list6)
print(list7)