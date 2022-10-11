phone = {"name" : "갤럭시","verison":"플립"}
if phone.get("name") == "갤럭시":
    if phone.get("verison")=="플립":
        print("접히네요")
    elif phone.get("verison")!="플립":
        print("좋네요")
else:
    print("와우")


#합
# list1 = [9,4,2,1,6,7,5,4,3,7]
# sum = 0

# for el in list1:
#     sum +=  el
# if sum % 2==0:
#     print(sum*2)

# else:
#     print(list1) 

list1 = [9,4,2,1,6,7,5,4,3,7]
list2 = []
i = 0
sum = 0 

while i < len(list1):
    sum += list1[i]
    # i = 0 , sum = 0 ,list1[i]= 9 
    # i = 1 , sum = 9 ,list1[i]= 4 
    # i = 2 , sum = 13 ,list1[i]= 2 
    # i = 3 , sum = 15,list1[i]= 1 
    # i = 4 , sum = 16 ,list1[i]= 6 
    if list1[i] % 2== 1:
        
        list2.append(list1[i]*2)
        
    else:
        list2.append(list1[i])
    i+=1
    if sum > 20 :
        continue
print(list2)
        