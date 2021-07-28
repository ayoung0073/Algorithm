## 1. 브루트포스 916 ms	14.4 MB
from itertools import combinations
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_gap = 10000
        ans = 0
        for arr in combinations(nums, 3):
            sum_val = sum(arr)
            if abs(sum_val - target) < min_gap:
                ans = sum_val
                min_gap = abs(sum_val - target)
                if min_gap == 0:
                    break
        return ans
            


## 2. 투 포인터 116 ms	14.4 MB
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_gap = 10 ** 3
        length = len(nums)
        ans = 0
        for i in range(length):
            left = i + 1
            right = length - 1
            
            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]
                gap = abs(target - sum_val)
                if sum_val == target:
                    return sum_val
                elif sum_val > target:
                    right -= 1
                else:
                    left += 1
                    
                if gap < min_gap:
                    min_gap = gap
                    ans = sum_val
                
        return ans
