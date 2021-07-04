# 524 ms	14.5 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        
        ans = 1
        
        for i in range(length):
            string = ""
            check = True
            for j in range(i, length):
                if s[j] in string:
                    ans = max(j - i, ans)
                    i = j + 1 # 시작 문자열 인덱스 변경
                    break
                if j == length - 1: 
                    ans = max(j - i + 1, ans)
                    
                string += s[j]
                
        return ans    
