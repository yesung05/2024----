Rpepper = int(input())
RpepperPrice = int(input())
chickBundle = int(input())
ChickPrice = int(input())

GotValue = Rpepper * RpepperPrice #고추 총 가격
ableBundleCnt = GotValue // ChickPrice

print(ableBundleCnt*chickBundle) #출력
