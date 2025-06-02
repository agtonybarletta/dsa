from typing import List
from unittest import TestCase


class Solution:
    """
    Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0
    If there are multiple solutions, return any of them.

     

    Example 1:

    Input: nums = [1,2,3]
    Output: [1,2]
    Explanation: [1,3] is also accepted.
    Example 2:

    Input: nums = [1,2,4,8]
    Output: [1,2,4,8]
     

    Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 2 * 109
    All the integers in nums are unique.
    """
    
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        lds = []
        nums.sort()
        N = len(nums)
        
        dp = [(0,0)]*N

        for i, n in nums:
            max_dp = (0,0)
            for k, m in range(nums[:i+1]):
                if m%k ==0 and dp[k] + 1 > max_dp:
                    max_dp = (dp[k] : + 1, k)
            dp[i] = max_dp
        




if __name__ == "__main__":

    # Input: nums = [1,2,3]
    # Output: [1,2]

    test_case = {'input': {'nums': [1,2,3]},  'expected': [1,2]}
    output = Solution().largestDivisibleSubset(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    # Input: nums = [1,2,4,8]
    #Output: [1,2,4,8]

    test_case = {'input': {'nums': [1,2,4,8]},  'expected': [1,2,4,8]}
    output = Solution().largestDivisibleSubset(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])
    
    test_case = {'input': {'nums': [4,8,10,240]},  'expected': [4,8,240]}
    output = Solution().largestDivisibleSubset(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    
