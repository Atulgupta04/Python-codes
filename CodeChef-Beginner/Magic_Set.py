#https://www.codechef.com/problems/MGCSET
t=int(input())
for _ in range(0,t):
        arr=[int(x) for x in input().split()]
        num=[int(x) for x in input().split()]
        count=0
        for j in num:
            if j%arr[1]==0:
                count+=1
        print((2**count)-1)
