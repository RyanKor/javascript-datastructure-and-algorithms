# https://programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    score = []
    n = ''
    for i in dartResult:
        if i.isnumeric(): # 테스트케이스가 숫자만 있거나 알파벳, 특수문자 만나기 전까지
            n += i
        elif i == 'S': # single -> 1 제곱
            score.append(int(n) ** 1)
            n = '' # n 초기화
        elif i == 'D': # double -> 2 제곱
            score.append(int(n) ** 2)
            n = '' # n 초기화
        elif i == 'T': # triple -> 3 제곱
            score.append(int(n) ** 3)
            n = '' # n 초기화
        elif i == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
        elif i == '#':
            score[-1] *= -1
    return sum(score)