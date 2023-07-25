from collections import deque
import sys
n = int(sys.stdin.readline())
a = deque(map(int,sys.stdin.readline().split()))

m= int(sys.stdin.readline())
b = deque(map(int,sys.stdin.readline().split()))

for i in range (len(b)):
    num = b[i]
    b[i] = a.count(num)

for i in range(len(b)):
    print(b[i] ,sep= '')
print (*b, sep=' ')