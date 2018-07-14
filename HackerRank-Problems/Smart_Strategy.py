#https://www.codechef.com/problems/SMRSTR
for i in range(int(input())):
	n, q = map(int,input().split())
	d=list(map(int,input().split()))
	x=list(map(int,input().split()))
	for j in range(q):
		for k in range(n):
			x[j] = x[j]//d[k]
		print(x[j],end=' ')
	print("")
