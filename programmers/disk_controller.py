# https://programmers.co.kr/learn/courses/30/lessons/42627

def solution(jobs):
    answer = 0
    start = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])  # 작업 소요시간 기준 정렬

    while len(jobs) != 0:
        for i in range(len(jobs)):
            # 현재까지 진행한 작업 진행 시간 총합 보다 먼저 프로세스가 들어온 경우다.
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0] # 전체 작업량만큼 추가
                jobs.pop(i) # 작업이 마무리 되면, 해당 작업은 삭제
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1

    return answer // length