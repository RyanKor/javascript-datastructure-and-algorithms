import sys
from itertools import permutations
# 1차 시도 -> 순열을 활용한 정답 풀이 : 메모리 초과
string = list(sys.stdin.readline().rstrip())
answer = []
comb = list(set(permutations(string, len(string))))
for palindrome in comb:
    if ''.join(palindrome) == ''.join(palindrome)[::-1]:
        answer.append(''.join(palindrome))
answer.sort()
if answer ==[]:
    print("I'm Sorry Hansoo")
else:
    print(answer[0])