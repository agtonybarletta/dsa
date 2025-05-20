from typing import List
from unittest import TestCase

class Solution:
    """
    You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

    For each queries[i]:

    Select a subset of indices within the range [li, ri] in nums.
    Decrement the values at the selected indices by 1.
    A Zero Array is an array where all elements are equal to 0.

    Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

    Example 1:
    Input: nums = [1,0,1], queries = [[0,2]]
    Output: true

    Explanation:

    For i = 0:
    Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
    The array will become [0, 0, 0], which is a Zero Array.
    Example 2:

    Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]
    Output: false

    Explanation:
    For i = 0:
    Select the subset of indices as [1, 2, 3] and decrement the values at these indices by 1.
    The array will become [4, 2, 1, 0].
    For i = 1:
    Select the subset of indices as [0, 1, 2] and decrement the values at these indices by 1.
    The array will become [3, 1, 0, 0], which is not a Zero Array.

    Constraints:

    1 <= nums.length <= 105
    0 <= nums[i] <= 105
    1 <= queries.length <= 105
    queries[i].length == 2
    0 <= li <= ri < nums.length
    """

    # def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
    #     """
    #     SOLUTION 1.
    #     O(nlogn): queries need to be sorted to be parsed according to this logic
    #     """
    #     queries.sort(key=lambda i: i[0])

    #     # subtraction arrays, what needs to be subtracted from nums
    #     sub = [0] * len(nums)

    #     # least recently opened interval
    #     lro_heap = []
    #     # lelf = left index of the opened interval
    #     left = 0
    #     # opened queries
    #     opened = 0

    #     # parse queries and build sub
    #     for q in queries:

    #         # close queries that needs to be closed
    #         while len(lro_heap) > 0 and q[0] > lro_heap[0]:
    #             right = heapq.heappop(lro_heap)
    #             while left <= right:
    #                 sub[left] = opened
    #                 left += 1
    #             opened -= 1

    #         # advance left up to q[0]
    #         while left < q[0]:
    #             sub[left] = opened
    #             left += 1

    #         # open q interval
    #         opened += 1
    #         heapq.heappush(lro_heap, q[1])

    #     # close all the opened intervals
    #     while len(lro_heap) > 0:
    #         right = heapq.heappop(lro_heap)
    #         while left <= right:
    #             sub[left] = opened
    #             left += 1
    #         opened -= 1

    #     for i in range(len(nums)):
    #         # if true, then non zero array, return false
    #         # check if nums[i] - sub[i] > 0
    #         if nums[i] > sub[i]:
    #             return False
    #     return True

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        """
        SOLUTION 2.
        compute the sub array without sorting queries:
            parse queries and build deltas array
            sub = cumulative sum array

        then apply the check loop and return isZeroArray result
        """

        N = len(nums)
        sub = [0] * N
        delta = [0] * N

        for q in queries:
            delta[q[0]] += 1
            if q[1] < N-1:
                delta[q[1]+1] -= 1

        sub[0] = delta[0]
        for i in range(1, N):
            sub[i] = sub[i-1] + delta[i]

        for i in range(N):
            # if true, then non zero array, return false
            # check if nums[i] - sub[i] > 0
            if nums[i] > sub[i]:
                return False
        return True


if __name__ == "__main__":

    test_case = {'input': {'nums': [1,0,1], 'queries': [[0,2]]},  'expected': True}
    output = Solution().isZeroArray(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    test_case = {'input': {'nums': [4,3,2,1], 'queries': [[1,3],[0,2]]}, 'expected': False}
    output = Solution().isZeroArray(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    test_case = {'input': {'nums': [2], 'queries': [[0,0],[0,0]]}, 'expected': True}
    output = Solution().isZeroArray(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])
    
