import sys

n = sys.stdin.readline()

print(str(oct(int("0b"+str(n), 2)))[2:])
