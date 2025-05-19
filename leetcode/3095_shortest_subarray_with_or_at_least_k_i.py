from typing import List
from unittest import TestCase


class Solution:
    """
    You are given an array nums of non-negative integers and an integer k.

    An array is called special if the bitwise OR of all of its elements is at least k.

    Return the length of the shortest special non-empty 
    subarray
    of nums, or return -1 if no special subarray exists.
    """

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        min_ = N+1
        for i in range(0, N):
            for j in range(i+1,N+1):
                or_ = 0
                for l in range(i, j):
                    or_ |= nums[l]
                if or_ >= k :
                    min_ = min(min_, j-i)
        return min_ if min_ < N+1 else -1

 
if __name__ == "__main__":
    """
    Example 1:
    Input: nums = [1,2,3], k = 2
    Output: 1
    Explanation:
    The subarray [3] has OR value of 3. Hence, we return 1.
    Note that [2] is also a special subarray.

    Example 2:
    Input: nums = [2,1,8], k = 10
    Output: 3
    Explanation:
    The subarray [2,1,8] has OR value of 11. Hence, we return 3.

    Example 3:
    Input: nums = [1,2], k = 0
    Output: 1
    Explanation:
    The subarray [1] has OR value of 1. Hence, we return 1.
    """
    print("Testcase 1")
    test_case_1 = {'input': {'nums': [1,  2,  3],  'k': 2},  'expected': 1}
    output = Solution().minimumSubarrayLength(**test_case_1['input'])
    TestCase().assertEqual(output, test_case_1['expected'])

    print("Testcase 2")
    test_case_2 = {'input': {'nums': [2,  1,  8],  'k': 10},  'expected': 3}
    output = Solution().minimumSubarrayLength(**test_case_2['input'])
    TestCase().assertEqual(output, test_case_2['expected'])

    print("Testcase 3")
    test_case_3 = {'input': {'nums': [1,  2],  'k': 0},  'expected': 1}
    output = Solution().minimumSubarrayLength(**test_case_3['input'])
    TestCase().assertEqual(output, test_case_3['expected'])

    print("Testcase 4")
    test_case_3 = {'input': {'nums': [8,  8, 8],  'k': 9},  'expected': -1}
    output = Solution().minimumSubarrayLength(**test_case_3['input'])
    TestCase().assertEqual(output, test_case_3['expected'])