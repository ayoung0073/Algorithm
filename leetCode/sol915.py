class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        length = len(nums)
        INF = 10**6
        min_arr = [INF for _ in range(length)]
        for i in range(length-2, -1, -1):
            min_arr[i] = min(nums[i], min_arr[i + 1])
        max_val = nums[0]            
        ans = 0
        
        while max_val > min_arr[ans + 1]:
            ans += 1
            max_val = max(max_val, nums[ans])
            
        return ans + 1
