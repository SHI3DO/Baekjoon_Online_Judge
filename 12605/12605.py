# Bronze I
import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    stack.append(' '.join(sys.stdin.readline().split()[::-1]))

o = 1
for j in stack:
    print(f"Case #{o}: {j}")
    o += 1
