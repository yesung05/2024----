expPrice = int(input())
relPrice = int(input())
diff = expPrice-relPrice
i=0
tmoney = 0
while(tmoney<relPrice):
    tmoney +=diff
    i += 1

print(i)