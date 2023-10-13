n=int(input())
n1=list(map(int,input().split()))
s=0
c=0
for i in n1:
    if i%2==0:
        s=s+i
    else:
        c=c+i
z=c-s
print(abs(z))