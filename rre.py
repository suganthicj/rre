x11=int(input())
l=list(map(int,input().split()))
y11=[]
for p in range(x11-1):
	y11.append(l[p]|l[p+1])
print(max(y11))
