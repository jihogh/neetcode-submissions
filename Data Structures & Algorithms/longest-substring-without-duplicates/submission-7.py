class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0

        current = set()

        longest = 0

        while r < len(s):
            while s[r] in current:
                current.remove(s[l])
                l += 1
            
            longest = max(longest, r-l+1)
            current.add(s[r])
            r += 1
        
        return longest