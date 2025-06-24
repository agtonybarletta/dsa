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

        # length of longest disible subset ending on index i
        dp = [1 for _ in  range(N)]
        # prev number of the divisible subset
        prev = [i for i in  range(N)]

        # the index i of the last element of the longest divisible subset
        best_i = 0 
        for i in range(N):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    # if improves
                    if dp[j] +1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[best_i] < dp[i]:
                best_i = i

        # reconstruct largest divisible subset by traversing prevs
        i = best_i
        lds.append(nums[i])
        while i != prev[i]:
            i = prev[i]
            lds.append(nums[i])
        return list(reversed(lds))





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

    test_case = {'input': {'nums': [5,9,18,54,108,540,90,180,360,720]},  'expected': [9,18,90,180,360,720]}
    output = Solution().largestDivisibleSubset(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    test_case = {'input': {'nums': [1]},  'expected': [1]}
    output = Solution().largestDivisibleSubset(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])
