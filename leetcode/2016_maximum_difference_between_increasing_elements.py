from typing import List
from unittest import TestCase


class Solution:
    """
    Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.

 

Example 1:

Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.


Example 2:

Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].


Example 3:

Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.


 

Constraints:

n == nums.length
2 <= n <= 1000
1 <= nums[i] <= 109
    """
    def maximumDifference(self, nums: List[int]) -> int:

        N = len(nums)
        # sliding window
        max_diff = -1 
        min_ = nums[0]

        for i in range(1, N):

            diff = nums[i] - min_
            # diff > 0 is a given constraing
            if diff > max_diff and diff > 0:
                max_diff = diff

            if nums[i] < min_:
                min_ = nums[i]

        return max_diff


if __name__ == "__main__":

    # Input: nums = [7,1,5,4]
    # Output: 4
    test_case = {'input': {'nums': [7,1,5,4] },  'expected': 4}
    output = Solution().maximumDifference(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    # Input: nums = [9,4,3,2]
    # Output: -1
    test_case = {'input': {'nums': [9,4,3,2]},  'expected': -1}
    output = Solution().maximumDifference(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])
