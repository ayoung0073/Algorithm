class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = set()
        for i in range(length - 3):
            for j in range(i + 1, length - 2):
                new_target = target - nums[i] - nums[j]
                s = j + 1
                e = length - 1
                while s < e:
                    if new_target == nums[s] + nums[e]:
                        ans.add((nums[i], nums[j], nums[s], nums[e]))     
                        s += 1
                        e -= 1
                    elif new_target > nums[s] + nums[e]:
                        s += 1
                    else:
                        e -= 1
        return ans
