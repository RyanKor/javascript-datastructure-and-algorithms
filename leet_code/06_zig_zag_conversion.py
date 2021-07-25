# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ''
        if numRows == 1:
            return s
        output = [[] for i in range(numRows)]

        direction = True
        count = 0
        for i in s:
            output[count].append(i)
            if direction:  # 각 배열 index 값에 하나씩 추가하기
                count += 1
            else:
                count -= 1  # 지그재그 위치 변경시키기
            if count == numRows:  # count 갯수가 num값과 같아졌다 == 이중 배열을 세로로 한번씩 순회했다.
                direction = False  # 방향 바꾸기
                count = max(numRows - 2, 0)  # 지그재그 값 추가
            if count <= 0:  # count가 0보다 작거나 같아지면
                direction = True
                count = 0  # 다시 세로방향으로 리스트 index 채우기
        for i in output:
            result += ''.join(i)

        return result