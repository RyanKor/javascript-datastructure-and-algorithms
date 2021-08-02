'''
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.


[예제]

N이 3일 경우,

1 2 3
8 9 4
7 6 5


N이 4일 경우,
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7

[제약사항]

달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
T = int(input())
for test_case in range(1, 1 + T):
    print('#{}'.format(test_case))
    N = int(input())
    my_map = [[0] * N for _ in range(N)]

    axis_x = [-1, 0, 1, 0]
    axis_y = [0, 1, 0, -1]
    x, y = 0, 0
    direction = 0

    for i in range(1, 1 + N**2):
        my_map[x][y] = i
        if 0 <= y + axis_y[direction] < N and 0 <= x + axis_x[
                direction] < N and my_map[x + axis_x[direction]][
                    y + axis_y[direction]] == 0:
            y += axis_y[direction]
            x += axis_x[direction]
        else:
            if direction == 3:
                direction = 0
            else:
                direction += 1

            y += axis_y[direction]
            x += axis_x[direction]

    for i in range(N):
        print(*my_map[i])