# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # 1. 중복된 i 값에 대한 계산은 건너 뛴다.
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                # 이 계산이 성립하는 이유는 위에서 매개변수 값을 정렬했기 때문이다.
                if sum < 0:
                    left +=1
                elif sum > 0:
                    right -=1
                # sum == 0이면 정답 및 스킵처리
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    
                    # 정답 값의 양 옆으로 동일한 값이 있을 수 있으므로 좌/우 값을 이동해서 스킵
                    while left< right and nums[left] == nums[left+1]:
                        left +=1
                    while left< right and nums[right] == nums[right-1]:
                        right -=1
                
                    # 현재 sum==0이기 때문에 좌/우에서 어느 한 쪽만 움직이는 것이 불가능하다.
                    left +=1
                    right -=1
        return result
                    