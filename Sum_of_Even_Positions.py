n=int(input())
s=0
n1=list(map(int,input().split()))
for i in range(0,n,2):
    a=n1[i]
    s=s+a
print(f'{s}')    