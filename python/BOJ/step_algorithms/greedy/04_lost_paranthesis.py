import sys

string = sys.stdin.readline().split("-")
answer = []

for i in string:
    temp = sum(list(map(int,i.split("+"))))
    answer.append(temp)

print(answer[0] - sum(answer[1:]))

'''
# 또 다른 풀이
import sys

string = sys.stdin.readline().split("-")
answer = 0

for i in range(len(string)):
    temp = sum(list(map(int, string[i].split("+"))))
    
    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)
'''