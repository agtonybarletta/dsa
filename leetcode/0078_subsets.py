from typing import List
from unittest import TestCase


class Solution:
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


Example 2:

Input: nums = [0]
Output: [[],[0]]


 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        N = len(nums)

        def gen(i: int, current: List[int]):
            if i >= N:
                ret.append(current[:])
                return

            gen(i+1, current)
            current.append(nums[i])
            gen(i+1, current)
            current.pop()
            return

        gen(0, [])
        return ret


if __name__ == "__main__":

    # Input: nums = [1,2,3]
    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    test_case = {'input': {'nums': [1,2,3]},  'expected': sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])}
    output = Solution().subsets(**test_case['input'])
    output.sort()
    TestCase().assertEqual(output, test_case['expected'])

