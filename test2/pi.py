def solution(n:int):
    answer = 1
    first =0
    second =1
    for i in range(2,n+1):
        answer = first+ second 
        #F(2) = F(0)+F(1)
        #F(3) = F(1)+F(2)
        first =second
        second = answer
    return answer %1234567
print(solution(3))