from typing import List
from unittest import TestCase


class Solution:
    """
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in place.

    Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

    Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1

    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        M = len(matrix[0])

        is_first_row_zero = False

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        is_first_row_zero = True
                    else:
                        matrix[i][0] = 0
        print(matrix)
        for i in range(1, N):
            for j in range(1, M):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        print(matrix)
        if matrix[0][0] == 0:
            for i in range(0, N):
                matrix[i][0] = 0

        print(matrix)
        if is_first_row_zero:
            for j in range(M):
                matrix[0][j] = 0

        print(matrix)


if __name__ == "__main__":

    test_case = {'input': {'matrix': [[1,1,1],[1,0,1],[1,1,1]]},  'expected': [[1,0,1],[0,0,0],[1,0,1]]}
    Solution().setZeroes(**test_case['input'])
    output = test_case['input']['matrix']
    TestCase().assertEqual(output, test_case['expected'])
    
    test_case = {'input': {'matrix': [[0,1,2,0],[3,4,5,2],[1,3,1,5]]},  'expected': [[0,0,0,0],[0,4,5,0],[0,3,1,0]]}
    Solution().setZeroes(**test_case['input'])
    output = test_case['input']['matrix']
    TestCase().assertEqual(output, test_case['expected'])

    test_case = {'input': {'matrix': [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]},  'expected': [[0,0,0,0,0],[0,0,0,0,0],[2147483647,2,-9,-6,0]]}
    Solution().setZeroes(**test_case['input'])
    output = test_case['input']['matrix']
    TestCase().assertEqual(output, test_case['expected'])

