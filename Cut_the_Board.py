#https://www.codechef.com/problems/CUTBOARD
t=int(raw_input())
for i in range (0,t):
    n,m=[int(X) for X in raw_input().split(" ")]
    print (n-1)*(m-1)
