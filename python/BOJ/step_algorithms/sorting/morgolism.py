import sys, operator

n = int(sys.stdin.readline())
answer = {}
for i in range(n):
    name, score = sys.stdin.readline().split()
    answer[name] = int(score)
# answer = dict(sorted(answer.items(), key=lambda x : (int(x[-1]), x[0])))
answer = dict(sorted(answer.items(), key=operator.itemgetter(1,0)))
rev_answer = dict(sorted(answer.items(), key=operator.itemgetter(1,0), reverse=True))
temp = []
for key, value in answer.items():
    temp.append(value)

if len(set(temp)) != len(temp):
    for key, value in answer.items():
        print(key)
        break
else:
    for key, value in rev_answer.items():
        print(key)
        break