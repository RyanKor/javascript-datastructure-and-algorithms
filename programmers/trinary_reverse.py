def solution(n):
    answer = 0
    trinary=convert(n, 3)[::-1]
    length = len(trinary)
    for i in range(len(trinary)):
        length -=1
        answer += int(trinary[i]) * (3**length)
        
    return answer
def convert(n, base):
    T = "0123456789ABCDEF"
    result = ''
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        result = convert(q, base) + T[r]
        return result