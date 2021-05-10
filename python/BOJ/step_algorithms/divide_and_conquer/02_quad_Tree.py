import sys
N = int(sys.stdin.readline())

image = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]


def quad_tree(x, y, n):
    # n = 1, 하나의 픽셀만 볼 경우,
    if(n == 1):
        return str(image[x][y])

    result = []
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 색이 다르면, 다시 분할하자.
            if(image[i][j] != image[x][y]):
                # append와 extend의 차이는
                # extend는 list, tuple, dict 등의 iterable object를
                # python list의 끝에 append 해주는 것.
                result.append('(')
                result.extend(quad_tree(x, y, n//2))
                result.extend(quad_tree(x, y + n//2, n//2))
                result.extend(quad_tree(x + n//2, y, n//2))
                result.extend(quad_tree(x + n//2, y + n//2, n//2))
                result.append(')')

                return result

    return str(image[x][y])


print(''.join(quad_tree(0, 0, N)))
