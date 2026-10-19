class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longest_l, longest_r = 0,0

        def check(l, r):
            nonlocal longest, longest_l, longest_r
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > longest:
                    longest_l = l
                    longest_r = r
                    longest = r-l+1
                l -= 1
                r += 1
            
        for i in range(len(s)):
            check(i,i)
            check(i,i+1)

        return s[longest_l:longest_r+1]