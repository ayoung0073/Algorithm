# Brute Force    4056 ms	14.9 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Hash      	52 ms	15.4 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist = {}
        for idx, val in enumerate(nums):
            other = target - val
            if other in exist:
                return [exist[other], idx]
            exist[val] = idx
        return []
