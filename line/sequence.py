'''
문제 설명
Sequence 최솟값 찾기
심심했던 브라운은 0~9의 숫자가 적혀 있는 쿠키를 이용해 1부터 N까지의 모든 수를 차례대로 나열했다. 그런데 브라운이 화장실 간 사이에 장난기 많은 샐리가 나열된 쿠키 중에서 마음에 드는 쿠키 몇 개를 먹어 버렸다. 화장실에 다녀온 브라운은 나열했던 쿠키 중 일부가 사라진 것을 알게 되었고, 이를 복구하기 위해 열심히 N을 떠올려 봤지만 기억나지 않았다. 결국 브라운은 남겨진 쿠키를 이용해서 최대한 복구해 보기로 결심했다.

브라운이 남겨진 쿠키를 이용해 복구할 수 있는 최소의 N을 구하는 프로그램을 작성하시오.

예시
브라운이 숫자 쿠키로 13까지 나열하면 다음과 같다.

12345678910111213

샐리가 아래 x로 표시한 위치의 쿠키를 먹었다고 가정하자.

전 : 브라운이 처음 나열한 쿠키
후 : 샐리가 일부의 쿠키를 먹은 이후
전	1	2	3	4	5	6	7	8	9	1	0	1	1	1	2	1	3
후	1	2	3	x	x	x	x	x	9	x	0	x	x	x	x	x	3
화장실에 다녀온 브라운은 아래와 같은 쿠키 배열을 발견할 것이다.

123903

브라운은 남겨진 쿠키를 이용해 최소의 N을 찾아야 한다.

입력 형식
123903

첫째 줄에 남겨진 수를 한 줄로 이어 붙인 수가 입력된다.
N은 1000 미만의 수이다.
첫 번째 값은 0으로 시작될 수 있다.
샐리가 아무것도 먹지 않았을 수 있다.
출력 형식
13

가능한 N 중에 최솟값을 출력한다.
'''

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