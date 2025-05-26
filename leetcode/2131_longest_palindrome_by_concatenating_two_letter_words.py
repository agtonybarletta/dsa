import collections
from typing import List
from unittest import TestCase


class Solution:
    """
    You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = [lc,cl,gg]
Output: 6
Explanation: One longest palindrome is lc + gg + cl = lcggcl, of length 6.
Note that clgglc is another longest palindrome that can be created.


Example 2:

Input: words = [ab,ty,yt,lc,cl,ab]
Output: 8
Explanation: One longest palindrome is ty + lc + cl + yt = tylcclyt, of length 8.
Note that lcyttycl is another longest palindrome that can be created.


Example 3:

Input: words = [cc,ll,xx]
Output: 2
Explanation: One longest palindrome is cc, of length 2.
Note that ll is another longest palindrome that can be created, and so is xx.


 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
    """
    def longestPalindrome(self, words: List[str]) -> int:

        count = collections.defaultdict(int)
        single = 0
        ret = 0
        for w in words:
            t = (w[0], w[1])
            if w[0] == w[1]:
                if count[t] > 0:
                    count[t] -= 1
                    single -= 1
                    ret += 4
                else:
                    count[t] += 1
                    single += 1
            else:
                it = (w[1], w[0])
                if count[it] > 0:
                    ret += 4
                    count[it] -= 1
                else:
                    count[t] += 1
        return ret + min(1, single)*2
        """
        # two dictionary not needed
        diff = collections.defaultdict(int)
        equals = collections.defaultdict(int)
        # we can process and count in 1 loop
        for w in words:
            t = (w[0], w[1])
            if w[0] == w[1]:
                equals[t] += 1
            else:
                diff[t] += 1
        count = 0
        
        couples = 0
        singles = 0

        # needless loop
        for k, n in equals.items():
            if n >= 2:
                couples += n//2
                singles += n%2
            else:
                singles += 1

        # needless loop
        for w, n in diff.items():
            t = (w[1], w[0])
            if t in diff:
                to_be_used = min(n, diff[t]) 
                count += to_be_used * 2
                diff[w] -= to_be_used
                diff[t] -= to_be_used

        # final formula con be simplified
        return (count + couples*2 + min(singles, 1))*2
        """

        
if __name__ == "__main__":

    # Input: words = [lc,cl,gg]
    # Output: 6
    test_case = {'input': {'words': ["lc","cl","gg"]},  'expected': 6}
    output = Solution().longestPalindrome(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])


    # ["cc","ll","xx"]
    test_case = {'input': {'words': ["cc","ll","xx"]},  'expected': 2}
    output = Solution().longestPalindrome(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    test_case = {'input': {'words': ["em","pe","mp","ee","pp","me","ep","em","em","me"]},  'expected': 14}
    output = Solution().longestPalindrome(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])
