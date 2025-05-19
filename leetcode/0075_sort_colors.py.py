from typing import List
from unittest import TestCase

class Solution:
    """
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.

     

    Example 1:

    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    Example 2:

    Input: nums = [2,0,1]
    Output: [0,1,2]
     

    Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.
    """

    def heapify(self, nums, n, i):

        l = i*2+1
        r = i*2+2
        
        largest = i
        if l < n and nums[l] > nums[largest]:
            largest = l
        
        if r < n and nums[r] > nums[largest]:
            largest = r
        
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, n, largest)
        
        
        

    def sortColors(self, nums: List[int]) -> None:
        
        # heapify all array
        N = len(nums)
        for i in range(N//2 +1, -1, -1):
            self.heapify(nums, N, i)


        for i in range (N-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
        return



    
if __name__ == "__main__":

    test_case = {'input': {'nums': [2,0,2,1,1,0]},  'expected': [0,0,1,1,2,2]}
    Solution().sortColors(**test_case['input'])
    output = test_case['input']['nums']

    TestCase().assertEqual(output, test_case['expected'])

    test_case = {'input': {'nums': [2,0,1]}, 'expected': [0,1,2]}

    Solution().sortColors(**test_case['input'])
    output = test_case['input']['nums']

    TestCase().assertEqual(output, test_case['expected'])
