n=int(input())
n1=list(map(int,input().split()))
s=0
for i in n1:
    if i%2==0:
        s=s+i
print(s)        