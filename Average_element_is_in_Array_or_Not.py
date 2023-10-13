n=int(input())
n1=list(map(int,input().split()))

n2=sum(n1)
c=n2//7
print(c in n1)
