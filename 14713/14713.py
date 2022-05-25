# Silver III
from collections import deque
import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(deque(map(str, sys.stdin.readline().split())))

sentence = deque(map(str, sys.stdin.readline().split()))

for j in range(len(sentence)):
    for i in range(0, n):
        if arr[i] and sentence:
            if arr[i][0] == sentence[0]:
                sentence.popleft()
                arr[i].popleft()

p = 0
for i in range(len(arr)):
    if len(arr[i]) > 0:
        p += 1

if len(sentence) > 0 or p > 0:
    print("Impossible")
else:
    print("Possible")
