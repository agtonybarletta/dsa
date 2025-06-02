from functools import lru_cache
from typing import List
from unittest import TestCase


class Solution:
    """
    2560. House Robber IV

    There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.
    The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.
    You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.
    You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.
    Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

     

    Example 1:

    Input: nums = [2,3,5,9], k = 2
    Output: 5
    Explanation: 
    There are three ways to rob at least 2 houses:
    - Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
    - Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
    - Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
    Therefore, we return min(5, 9, 9) = 5.
    Example 2:

    Input: nums = [2,7,9,3,1], k = 2
    Output: 2
    Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
     

    Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= (nums.length + 1)/2
    """

    def minCapability(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        INF = 110
        
        memo ={}
        
        @lru_cache(maxsize=None)
        def dp(i, r):
            # If we have picked enough houses, our "capability" is 0.
            if r == 0:
                return 0
            # If there are no houses left but we need more, return INF.
            if i >= n:
                return INF
            
            # Option 1: Skip the current house.
            skip = dp(i + 1, r)
            # Option 2: Rob the current house, then skip the next one.
            rob = max(nums[i], dp(i + 2, r - 1))
            
            return min(skip, rob)
        
        return dp(0, k)
        
        """
        def rec(i, j):
            if i == N:
                return MAX
            if i == N-1:
                return nums[i]
            if (i,j) in memo:
                return memo[(i,j)]

            min_value = min( max(nums[i], rec(i+2, j+1)), rec(i+1, j))
            memo[(i,j)] = min_value
            return min_value
        rec(0, 0)
        print(memo)
        return 0
        """

if __name__ == "__main__":

    print("Testcase 1")
    test_case_1 = {'input': {'nums': [2,3,5,9], 'k': 2},  'expected': 5}
    output = Solution().minCapability(**test_case_1['input'])
    TestCase().assertEqual(output, test_case_1['expected'])
