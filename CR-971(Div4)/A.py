import sys
input=lambda:sys.stdin.readline().rstrip()

t = int(input())
while t > 0:
    a, b = map(int, input().split())
    print(b - a)
    t -= 1
