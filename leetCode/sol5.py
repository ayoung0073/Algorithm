# 96 ms	14.5 MB
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 1
        start = 0
        
        for i in range(len(s)):
        	if i - maxLen >= 1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start = i-maxLen-1
        		maxLen += 2
        		continue

        	if i-maxLen >= 0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start = i - maxLen
        		maxLen += 1
                
        return s[start:start+maxLen]

# ME ...
# 9132 ms	14.4 MB
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for start in range(len(s)):
            for end in range(len(s), start, -1):
                sub = s[start:end + 1]
                if sub == sub[::-1]:
                    if len(ans) < end - start + 1:
                        ans = sub
                    break

        return ans
        
