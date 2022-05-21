# Silver III
import sys

s = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
stack = []
p = len(s)
for i in range(n):
    gb = sys.stdin.readline().split()

    if gb[0] == 'L':
        if len(s) > 0:
            stack.append(s.pop())
    if gb[0] == 'D':
        if len(stack) > 0:
            s.append(stack.pop())
    if gb[0] == 'B':
        if len(s) > 0:
            s.pop()
    if gb[0] == 'P':
        s.append(gb[1])

print(''.join(s + list(reversed(stack))))
