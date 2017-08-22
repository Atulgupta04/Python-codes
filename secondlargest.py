#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)
