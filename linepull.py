from itertools import combinations

def splitAry(arr):
    n = len(arr)

    mdiff = float('inf')  #최대값이 지정되어 있지 않기에 
    rlst1 = [] #realAry
    rlst2 = []

    lst1Len = n // 2
    lst2Len = n - lst1Len
    
    for size in range(lst1Len, lst2Len + 1):  
        for tup in combinations(arr, size):
            ary1Sum = sum(tup)
            subset2 = [x for x in arr if x not in tup] #arr
            ary2Sum = sum(subset2)
            
            diff = abs(ary1Sum - ary2Sum) #차
            
            # 합의 차이가 더 작은 경우 반영영
            if diff < mdiff:
                mdiff = diff
                rlst1 = list(tup)
                rlst2 = subset2
    
    # 결과 반환
    arys = [sum(rlst1),sum(rlst2)]
    arys.sort()
    return arys

arr = list(map(int,input().split()))

sum = splitAry(arr)
print(sum[0], sum[1])
