from typing import List
from unittest import TestCase


class Solution:
    """
    You are given an integer array height of length n.
    There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.

    Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

    Example 2:
    Input: height = [1,1]
    Output: 1

    Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
    """

    def maxArea(self, height: List[int]) -> int:

        N = len(height)
        l = 0
        r = N-1

        max_a = 0
        while l < r:
            current_a = min(height[l], height[r]) * (r-l)

            if current_a > max_a:
                max_a = current_a

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return max_a


if __name__ == "__main__":

    # Input: height = [1,8,6,2,5,4,8,3,7]
    # Output: 49
    test_case = {'input': {'height': [1,8,6,2,5,4,8,3,7]},  'expected': 49}
    output = Solution().maxArea(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    # Input: height = [1,1]
    # Output: 1
    test_case = {'input': {'height': [1,1]},  'expected': 1}
    output = Solution().maxArea(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])
