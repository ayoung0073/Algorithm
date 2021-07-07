# 100 ms	14.6 MB
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        one, two = 0, 0
        merged_arr = []
        
        while one < m and two < n:
            if nums1[one] < nums2[two]:
                merged_arr.append(nums1[one])
                one += 1
            elif nums1[one] > nums2[two]:             
                merged_arr.append(nums2[two])
                two += 1
            else:
                merged_arr.append(nums1[one])
                merged_arr.append(nums2[two])
                one += 1
                two += 1
        
        while one < m:
            merged_arr.append(nums1[one])
            one += 1
               
        while two < n:
            merged_arr.append(nums2[two])
            two += 1     
            
        if (m + n) % 2 == 0: # 짝수인 경우
            return (merged_arr[(m + n) // 2] + merged_arr[(m + n) // 2 - 1]) / 2
        else:
            return merged_arr[(m + n) // 2]
