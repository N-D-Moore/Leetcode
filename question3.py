#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        x = 0
        longest = 0

        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[x])
                x += 1
            window.add(s[i])
            longest = max(longest, i-x+1)
        return longest