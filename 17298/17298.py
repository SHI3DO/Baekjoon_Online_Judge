# Gold IV
import sys

n = int(input())
a = [-1] * n
np = list(map(int, sys.stdin.readline().split()))
stack = [0]

for i in range(1, n):
    while stack and np[stack[-1]] < np[i]:
        a[stack.pop()] = np[i]
    stack.append(i)

print(*a)
