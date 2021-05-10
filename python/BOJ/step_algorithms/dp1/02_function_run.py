'''
문제
재귀 호출만 생각하면 신이 난다! 아닌가요?

다음과 같은 재귀함수 w(a, b, c)가 있다.

if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns: (셋 중 하나가 0 또는 음수라면 결과 값은 무조건 1이다)
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:  (셋 중 하나가 20보다 큰 양수라면 w(20,20,20) 값을 출력)
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)

a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.

입력
입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

출력
입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.

w(1, 1, 1) = 2
w(2, 2, 2) = 4
w(10, 4, 6) = 523
w(50, 50, 50) = 1048576
w(-1, 7, 18) = 1
##################

제한
-50 ≤ a, b, c ≤ 50

* 문제 풀이 시, 유의사항 *
- 문제 풀이 중에 재귀함수가 떠오른다면, 아마 많은 경우에 동적 프로그래밍을 통해 문제를 풀어야할 것이다
- 이유야 많겠지만, 동적 프로그래밍의 경우 문제 풀이 시간이 초과되는 경우를 막고, 연산 속도를 높이기 때문이다.

재귀함수를 사용해야할 때 이것을 메모이제이션 하는 방법을 묻는 문제
'''

MAX = 21
dp = [[[0]*MAX for _ in range(MAX)] for __ in range(MAX)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 값이 이미 존재한다면 그 값을 바로 리턴.
    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
        w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]


while True:

    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))

print(dp)
