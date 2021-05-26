def solution(operations):
    answer = []

    for i in operations:
        temp = i.split()
        if temp[0] == "I":
            answer.append(int(temp[-1]))
        elif temp[0] == "D" and temp[-1] == '1':
            if answer == []:
                pass
            else:
                answer.remove(max(answer))
        elif temp[0] == "D" and temp[-1] == '-1':
            if answer == []:
                pass
            else:
                answer.remove(min(answer))
    if answer == []:
        return [0,0]
    else:
        return [max(answer),min(answer)]