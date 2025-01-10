def Calcladder(A, B, C):
    pos = A
    pos -= B
    pos += C
    pos = pos*2+1
    return pos

print(Calcladder(int(input()),int(input()),int(input())))