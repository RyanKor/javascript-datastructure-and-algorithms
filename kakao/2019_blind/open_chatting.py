# https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    users = dict()
    for re in record:
        if re[0] == 'E' or re[0] == 'C':
            op, userid, nickname = re.split()
            users[userid] = nickname
    for re in record:
        who = re.split()[1]
        if re[0] == 'E':
            answer.append("{}님이 들어왔습니다.".format(users[who]) )
        if re[0] == 'L':
            answer.append("{}님이 나갔습니다.".format(users[who]))
    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))