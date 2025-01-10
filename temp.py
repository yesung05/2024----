import operator

ops = {'+': operator.add,'-': operator.sub}


def get_comb(num1, op1, op2):
    values = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if ops[op2](ops[op1](i, j), k) == num1:
                    values.append((i, j, k))
    return values

def get_result(num1, num2, num3, num4, num5, num6):

    values = []
    for n1 in num1:
        a = n1[0]
        b = n1[1]
        c = n1[2]
        for n2 in num2:
            d = n2[0]
            e = n2[1]
            f = n2[2]
            for n3 in num3:
                g = n3[0]
                h = n3[1]
                i = n3[2]
                values = [a, b, c, d, e, f, g, h, i]
                if len(set(values)) == 9:
                    for n4 in num4:
                        if n4[0] == a and n4[1] == d and n4[2] == g:
                            for n5 in num5:
                                if n5[0] == b and n5[1] == e and n5[2] == h:
                                    for n6 in num6:
                                        if n6[0] == c and n6[1] == f and n6[2] == i:
                                            return values
    return values

inputs = list(map(int,input().split()))


abcComb = get_comb(inputs[0], '+','-')
defComb = get_comb(inputs[1], '+', '+')
ghiComb = get_comb(inputs[2], '-', '+')
adgComb = get_comb(inputs[3], '-','+')
behComb = get_comb(inputs[4], '+', '-')
cfiComb = get_comb(inputs[5], '+', '+')

rowsCount = len(abcComb) * len(defComb) * len(ghiComb) 
ColumCount = len(adgComb) * len(behComb) * len(cfiComb)

if rowsCount <= ColumCount:
    value = get_result(abcComb, defComb, ghiComb, adgComb, behComb, cfiComb)
    
    rstary = [value[0], value[1], value[2], value[3], value[4], value[5],value[6], value[7], value[8]]


else:
    value = get_result(adgComb, behComb, cfiComb, abcComb, defComb, ghiComb)
    rstary = [value[0], value[3], value[6],value[1], value[4], value[7],value[2], value[5], value[8]]

for val in rstary:
    print(val, end=' ')

