import sys
from itertools import product

n = int(sys.stdin.readline())
binary = ['0','1']
answer = []
if n == 1:
    print(1)
if n == 2:
    print(2)

arr = list(product(binary,repeat=n))
for i in arr:
    temp = ''.join(i)
    if temp.count('0') % 2 !=0:
        pass
    elif '00' in temp:
        answer.append(temp)
    elif temp.count('1') == n:
        answer.append(temp)
print(len(answer))