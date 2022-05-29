import sys

n = sys.stdin.readline()

k = sys.stdin.readline().split()
f = []
for i in range(len(k)):
    f.append(int(k[i]))

print(min(f)*max(f))