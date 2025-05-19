from unittest import TestCase
from typing import List
from functools import cache
"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)

        def recursive(i):
            if i >= n:
                return True
            ans = False
            for w in wordDict:
                start = i
                end = i+len(w)
                if s[start:end] == w and recursive(end):
                    return True
            return ans
        return recursive(0)
        """
        recursion on every start and end, bad solution
        @cache
        def recursive(start, end):
            if end >= n:
                if start == end:
                    return True
                else:
                    return False

            ans = False
            
            ans = ans or recursive(start, end+1)
            if s[start:end+1] in wordDict:
                ans = ans or recursive(end+1, end+1)
            return ans
        return recursive(0, 0)
        """


if __name__ == "__main__":
    
    s = "leetcode"
    wordDict = ["leet","code"]
    
    expected = True
    output = Solution().wordBreak(s, wordDict)

    TestCase().assertEqual(output, expected)
