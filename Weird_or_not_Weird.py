a=int(input())
if a%2!=0:
    print('weird')
elif a in  (2 , 4):
    print('not weird')
elif a in (6,8,10,12,14,16,18,20):
    print('weird')
elif (a>20):
    print('not weird')