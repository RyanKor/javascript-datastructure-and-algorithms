# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: List[int]) -> int:
        #         volume = 0
        #         stack = []

        #         for i in range(len(height)):
        #             while stack and height[i] > height[stack[-1]]:
        #                 top = stack.pop()

        #                 if len(stack) == 0:
        #                     break

        #                 distance = i - stack[-1] - 1

        #                 waters = min(height[i],height[stack[-1]]) - height[top]

        #                 volume += distance * waters

        #             stack.append(i)

        #         return volume

        if len(height) == 0:
            return 0
        # two pointer는 기본적으로 많이 풀어봤으니까 이해가 더 잘되는 것이다.
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume