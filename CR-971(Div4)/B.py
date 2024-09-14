"""
https://codeforces.com/contest/2009/problem/D
"""

import sys
input=lambda:sys.stdin.readline().rstrip()

t: int = int(input())
for _ in range(t):
    li = []
    n = int(input())
    for _ in range(n):
        s = input()
        li.append(s.index('#')+1)
    for i in range(len(li)-1, -1, -1):
        print(li[i], end=' ')
    print()

