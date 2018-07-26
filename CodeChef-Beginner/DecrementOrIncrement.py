#https://www.codechef.com/problems/DECINC
n = int(input())
if n % 4 == 0:
    n=n+1
    print(n)
elif n%4 != 0:
    n=n-1
    print(n)
