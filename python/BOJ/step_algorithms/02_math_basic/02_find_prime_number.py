'''
문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
'''

import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

result = []
cnt = 0

for i in range(M, N+1):  # 아니 여기서 왜 range를 빼먹어서 애먹게하나..;
    count = 0
    if i == 1:
        pass
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
            if count > 2:  # 이 코드를 추가 안하면, 반드시 에러가 발생한다.
                break
    if count == 1:
        result.append(i)

if result == []:
    print(-1)
else:
    print(sum(result))
    # 굳이 정렬할 필요가 없다. 범위 내의 숫자에서 작은 수에서 큰 수로 확장해나가는 구조라 수의 크기로 정렬이 필요 없기 때문
    print(result[0])
