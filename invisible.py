def TimeCalc(spds):

    spds.sort() #빠른 순서로 정렬렬

    n = len(spds)

    time = 0

    while n > 3:
        tmp1 = 2 * spds[1] + spds[0] + spds[n-1] #최소 시간을 위하여 비교 위한 temp
        tmp2 = 2 * spds[0] + spds[n-2] + spds[n-1] 
        
        time += min(tmp1, tmp2)
        n -= 2  
    
    if n == 3:
        time += spds[2] + spds[1] + spds[0]

    elif n == 2:
        time += spds[1]

    else:
        time += spds[0]
    
    return time


spds = list(map(int,input().split()))

print(TimeCalc(spds)) #함수 사용 출력
