

s = "sssss"
n = "nnnnn"
print(s)
print(n)
# 주석#################################

a = [1,1,2,3,4,2,1,4,5,6,7,8,10]
set(a)
print(a)
a= {'name': 'kim', 'score': 50}
b= {'name': 'kim', 'score': 50}
c= {'name': 'kim', 'score': 50}
print("%s는 점수가 80점 이상이 %s"%(a.get("name"),a["score"]>=80))
print("%s는 점수가 80점 이상이 %s"%(b.get("name"),b["score"]>=80))
print("%s는 점수가 80점 이상이 %s"%(c.get("name"),c["score"]>=80))
