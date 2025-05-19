from typing import List
from unittest import TestCase


class Solution:
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

    Example 1:

    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    Example 2:

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
    Example 3:

    input: nums = [1,0,1,2]
    output: 3
    """

    def longestConsecutive(
        self,
        nums: List[int]
    ) -> int:

        s = set(nums)
        longst_consecutive = 0
        for i in s:
            if i - 1 not in s:
                j = i
                current_consecutive = 0
                while j in s:
                    current_consecutive += 1
                    j += 1
                if j - i > longst_consecutive:
                    longst_consecutive = j - i
        return longst_consecutive


if __name__ == "__main__":

    test_case = {'input': {'nums': [100, 4, 200, 1, 3, 2]},   'expected': 4}
    output = Solution().longestConsecutive(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    test_case = {'input': {'nums': [0,3,7,2,5,8,4,6,0,1]},   'expected': 9}
    output = Solution().longestConsecutive(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    test_case = {'input': {'nums': [1,0,1,2]},   'expected': 3}
    output = Solution().longestConsecutive(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])