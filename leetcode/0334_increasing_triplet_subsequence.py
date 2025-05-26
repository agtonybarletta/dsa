from typing import List
from unittest import TestCase
import sys


class Solution:
    """
    Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

    Example 1:

    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.
    Example 2:

    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.
    Example 3:

    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

    Constraints:

    1 <= nums.length <= 5 * 105
    -231 <= nums[i] <= 231 - 1

    Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
    """
    def increasingTriplet(self, nums: List[int]) -> bool:
        seq: List[int] = [sys.maxsize, sys.maxsize]
        
        for n in nums:
            if n <= seq[0]:
                seq[0] = n
            elif n <= seq[1]:
                seq[1] = n
            else:
                return True
        return False

if __name__ == "__main__":

    # Input: nums = [1,2,3,4,5]
    # Output: true
    test_case = {'input': {'nums': [1,2,3,4,5]},  'expected': True}
    output = Solution().increasingTriplet(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])


    # Input: nums = [5,4,3,2,1]
    # Output: false
    test_case = {'input': {'nums': [5,4,3,2,1]},  'expected': False}
    output = Solution().increasingTriplet(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    # Input: nums = [2,1,5,0,4,6]
    # Output: true
    test_case = {'input': {'nums': [2,1,5,0,4,6]},  'expected': True}
    output = Solution().increasingTriplet(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])


    test_case = {'input': {'nums': [1,1,1,1]},  'expected': False}
    output = Solution().increasingTriplet(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])