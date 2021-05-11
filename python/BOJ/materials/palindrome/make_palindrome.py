import sys
from itertools import permutations

string = list(sys.stdin.readline().rstrip())
# 1차 시도 -> 순열을 활용한 정답 풀이 : 메모리 초과
# answer = []
# comb = list(set(permutations(string, len(string))))
# for palindrome in comb:
#     if ''.join(palindrome) == ''.join(palindrome)[::-1]:
#         answer.append(''.join(palindrome))
# answer.sort()
# if answer ==[]:
#     print("I'm Sorry Hansoo")
# else:
#     print(answer[0])

# 2차 시도 -> 타인의 답을 확인하고 정답 풀이 : 
cnt = [0 for _ in range(26)] # 알파벳 갯수 만큼 cnt
for alphabet in string:
    cnt[ord(alphabet)-65] +=1

odd = 0
odd_alpha = ''
alpha = ''

for i in range(26):
    if cnt[i] % 2 == 1:
        odd +=1
        odd_alpha += chr(i+65)
    alpha += chr(i+65) * (cnt[i]//2)

if odd > 1: # 팰린드롬이 되려면 알파벳이 하나만 나오는 상황이 2개 이상이면 모두 예외 처리해야함
    print("I'm Sorry Hansoo")
else:
    print(alpha+odd_alpha+alpha[::-1]) # 알파벳이 하나만 나오는 상황이 1개 이하라면, 이 순서로 출력