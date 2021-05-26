# https://programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque 
def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    if cacheSize == 0: 
        return len(cities) * 5
    else: 
        for i in cities: 
            # 대소문자는 구분하지 않으므로 lower으로 변경 
            i = i.lower()
            if i in cache: 
                answer += 1
            else: 
                answer += 5 
            if i in cache: 
                cache.remove(i)
            else:
                if len(cache) >= cacheSize: 
                    cache.popleft()

            cache.append(i)
    return answer