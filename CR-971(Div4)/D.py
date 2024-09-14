"""
https://codeforces.com/contest/2009/problem/D
"""

import sys
input=lambda:sys.stdin.readline().rstrip()

t: int = int(input())
for _ in range(t):
    n: int = int(input())
    ds = [[False for p in range(n+1)] for q in range(3) ] # [dim(3 * n+1)]
    for __ in range(n):
        x, y = map(int, input().split())
        ds[y][x] = True # Marking coordinates as True

    count = 0
    for i in range(n+1):
        if ds[0][i] and ds[1][i]:
            # if x1=x2 is same but y1=0,y2=0 -> all other points except these two point
            # will be a right triangle
            count += n-2
        if 0 < i < n and ds[0][i] and ds[1][i - 1] and ds[1][i + 1]:
            """
            If i is between 1 and n-1, and for a point in (x,0) there are two points, 
            (x-1, 1) and (x+1, 1) -> the count is incremented by 1.
            """
            count += 1
        if 0 < i < n and ds[1][i] and ds[0][i-1] and ds[0][i+1]:
            """
            If i is between 1 and n-1, and for a point in (x,1) there are two points, 
            (x-1, 0) and (x+1, 0) -> the count is incremented by 1.
            """
            count += 1

    print(count)

