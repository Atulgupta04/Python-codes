#https://www.codechef.com/problems/NAICHEF
t = int(input())
for _ in range (t):
   n,a,b=map(int,input().split())
   number = list(map(int,input().split()))
   x=number.count(a)
   y=number.count(b)
   print('%0.10f'%((x*y)/(n*n)))
