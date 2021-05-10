import sys

alphabet = sys.stdin.readline().rstrip()
dic = {}
temp = []
for word in alphabet.upper():
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

dic_sorted = sorted(dic.items(), key=lambda item: item[1])

if len(dic_sorted) > 1 and dic_sorted[-1][-1] == dic_sorted[-2][-1]:
    print('?')
else:
    print(dic_sorted[-1][-2])
