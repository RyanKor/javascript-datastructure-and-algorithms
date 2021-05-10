'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
import sys

case = int(sys.stdin.readline())
result = []
for i in range(case):
    num = int(sys.stdin.readline())
    result.append(num)

for j in sorted(result):
    print(j)

# Wrong Answer -> 주어진 값이 항상 정렬되어 제공되지 않는 예외가 있었다.
# for j in range(len(result), 0, -1):
#     '''
#     range(10, 0)과 같이 시작하는 숫자를 큰 숫자로 지정하고 끝나는 숫자를 작은 숫자로 지정하면 숫자가 감소할 것 같은데 실행을 해보면 아무것도 출력되지 않습니다. 왜냐하면 range는 숫자가 증가하는 기본 값이 양수 1이기 때문입니다.

#     숫자를 역순으로 생성하려면 증가 폭을 음수로 지정하면 됩니다
#     '''
#     print(result[j-1])
