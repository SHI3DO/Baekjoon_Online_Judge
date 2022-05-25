# Silver IV
import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()
for i in range(n):
    cc = sys.stdin.readline().split()
    if cc[0] == 'push_front':
        queue.appendleft(cc[1])
    if cc[0] == 'push_back':
        queue.append(cc[1])
    if cc[0] == 'pop_front':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.popleft())
    if cc[0] == 'pop_back':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.pop())
    if cc[0] == 'size':
        print(len(queue))
    if cc[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if cc[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print("-1")
    if cc[0] == 'back':
        if len(queue) > 0:

            print(queue[len(queue) - 1])
        else:
            print("-1")
