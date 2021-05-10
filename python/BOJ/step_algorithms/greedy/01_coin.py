'''
문제
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

*처음으로 탐욕 알고리즘 기법을 아무 정답도 안찾아보고 풀어볼 수 있게 되었다.*
'''

import sys

test_case, total = map(int, sys.stdin.readline().split())
coin_type = []
index = len(coin_type) - 1
cnt = 0
for i in range(test_case):
    coin_type.append(int(sys.stdin.readline()))

while True:
    if coin_type[index] > total:
        pass
        index -= 1
    else:
        cnt = cnt + (total // coin_type[index])
        total = total % coin_type[index]

        if total <= 0:
            break
print(cnt)
