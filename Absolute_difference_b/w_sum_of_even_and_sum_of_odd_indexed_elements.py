n=int(input())
s=0
c=0
n1=list(map(int,input().split()))
for i in range(1,n,2):
    a=n1[i]
    s=s+a
for d in range(0,n,2):
    b=n1[d]
    c=c+b
z=c-s    
print(f"{z}")    