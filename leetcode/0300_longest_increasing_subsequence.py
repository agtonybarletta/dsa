from functools import cache
from typing import List
from unittest import TestCase

class Solution:
    """
    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    Example 1:

    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    Example 2:

    Input: nums = [0,1,0,3,2,3]
    Output: 4
    Example 3:

    Input: nums = [7,7,7,7,7,7,7]
    Output: 1
     

    Constraints:

    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

    """

    def lengthOfLIS(self, nums: List[int]) -> int:

        N = len(nums)

        dp = [0] * (N)
        dp[0] = 1

        for i in range(1, N):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    taken = dp[j] +1
                    dp[i] = max(dp[i], taken)
        return max(dp)


        """
        # return the length of LIS at index i, assuming the next larger element is prev
        # all the nums[i] of LIST must be <= largest
        # (LIST may not end in i)
        @cache
        def dp(i, largest):
            if i == -1:
                return 0
            
            # recurr without taking i
            ans = dp(i-1, largest)
            if nums[i] < largest:
                # recurr taking i 
                taken =  dp(i-1, nums[i]) +1
                ans = max(ans, taken)

            return ans

        return dp(N-1, float("inf"))
        """


        
    
if __name__ == "__main__":

    test_case = {'input': {'nums': [10,9,2,5,3,7,101,18]},  'expected': 4 }
    output = Solution().lengthOfLIS(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    test_case = {'input': {'nums': [0,1,0,3,2,3]},  'expected': 4 }
    output = Solution().lengthOfLIS(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])


    test_case = {'input': {'nums': [7,7,7,7,7,7,7]},  'expected': 1 }
    output = Solution().lengthOfLIS(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

