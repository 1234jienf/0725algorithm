import sys
from collections import deque
n = int(sys.stdin.readline())

s= deque()
# 1,2,3,..n 이 들어있는 카드 리스트 만들기
for i in range(1,n+1):
    s.appendleft(i)
# s 에 들어있는 숫자가 1개가 아니라면 맨끝 숫자를 앞으로 가져오고, 1개라면 print
while True:
    if len(s) != 1:
        s.pop()
        a=s.pop()
        s.insert(0,a)
    else:
        print(s[0])
        break