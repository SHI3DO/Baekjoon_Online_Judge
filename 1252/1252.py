import sys

a,b = sys.stdin.readline().split()

print(str(bin(int(a, 2) + int(b,2)))[2:])