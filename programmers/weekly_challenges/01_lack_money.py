# https://programmers.co.kr/learn/courses/30/lessons/82612


def solution(price, money, count):

    return abs(min(money - sum([i * price for i in range(1, count + 1)]), 0))
