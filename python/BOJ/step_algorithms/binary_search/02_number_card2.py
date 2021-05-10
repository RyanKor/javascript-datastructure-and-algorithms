'''
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.


# 시간 초과 코드 -> for loop만 써서 정리하려고 하면, 시간초과가 발생한다.
import sys

N = int(sys.stdin.readline())

card1 = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

card2 = list(map(int, sys.stdin.readline().split()))
result = []

for i in card2:
    result.append(card1.count(i))
print(*result)
'''

import sys

# 여기서 1차로 딕셔너리 정리를 해서 에러 발생이 안한건가?
N = int(sys.stdin.readline())
card1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card2 = list(map(int, sys.stdin.readline().split()))

dic = {}
result = []
for i in card1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in card2:
    if i in dic:
        result.append(dic[i])
    else:
        result.append(0)

print(*result)
