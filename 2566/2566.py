import sys

A = []
for i in range(9):
    A.append(sys.stdin.readline().split())

k = [0, 0, 0]
for i in range(9):
    for j in range(9):
        if int(A[i][j]) > int(k[0]):
            k.clear()
            k.append(A[i][j])
            k.append(i)
            k.append(j)

print(k[0])
print(k[1]+1, k[2]+1)
