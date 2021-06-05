def solution(inputString):
    answer = 0
    # 만약 inputString의 시작 값이 0부터 진행된다면
    # 앞 부분에서 sequence 최솟값을 찾으려면 0이 붙는 자리 수 중에 최솟 값인 10을 가정한다. (1<= N <= 1000)
    # 사라진 쿠키의 갯수를 세는 게 아니다! 쿠키가 본래 최소 몇 개 있었는지 확인하는 것
    # 언제 최소 갯수의 쿠키를 만들 수 있는가?
    digit_change = 0
    if inputString[0] == '0':
        digit_change = 1
    for i in range(len(inputString)):
        for j in range(i+1, len(inputString)):
            if inputString[i] < inputString[j]:
                break
            else: # 여기서 조건을 더 추가해야한다.
                if str(digit_change) == inputString[i] and inputString[i] > inputString[j]:
                    break
                else:
                    digit_change +=1
                    break      
    answer = int(str(digit_change) + inputString[-1])
    return answer