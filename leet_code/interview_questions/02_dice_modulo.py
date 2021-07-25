from itertools import product


def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


def numRollsToTarget(d, f, target):
    dice = range(1, f + 1)
    answer = 0

    products = combinations_with_replacement(dice, d)
    for i in products:
        if sum(i) == target:
            answer += 1
    return answer


print(numRollsToTarget(30, 30, 500))