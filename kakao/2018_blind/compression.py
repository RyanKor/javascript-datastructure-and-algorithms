def solution(msg):
    answer = []
    alphabet = [chr(i) for i in range(ord("A"), ord("Z")+1)] # 앞으로 알파벳 생성할 땐 이 방법을 따라가자.
    dic = {}
    for i in range(1,27):
        dic[alphabet[i-1]] = i
    idx = 0
    maxIdx = 26
    length = 0 # 단어 길이
    while True:
        length +=1
        if msg[idx:idx+length] not in dic:
            answer.append(dic[msg[idx:idx+length-1]]) # 현재 없는 값 앞 부분 출력을 위해 answer.append
            maxIdx +=1 # 신규 텍스트 추가를 위한 인덱스 증가
            dic[msg[idx:idx+length]] = maxIdx
            idx += length-1
            length =0
        else:
            if idx + length -1 == len(msg):
                answer.append(dic[msg[idx:idx+length-1]])
                break
    return answer

print(solution('TOBEORNOTTOBEORTOBEORNOT'))