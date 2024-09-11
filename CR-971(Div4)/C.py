import math
import sys
input=lambda:sys.stdin.readline().rstrip()

t: int = int(input())
for _ in range(t):
    x, y, k = map(int, input().split())
    xx = math.ceil(x / k)
    yy = math.ceil(y / k)

    # if x is greater than y, then we can skip one round of y
    if xx > yy:
        print(2*xx - 1)
    else:
        print(2*yy)
