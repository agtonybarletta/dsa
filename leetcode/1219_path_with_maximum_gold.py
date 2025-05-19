"""
1219. Path with Maximum Gold
Medium
Topics
Companies
Hint
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""
import collections
from typing import List
import unittest

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])
        visited = set()

        def allowed_cell(r,c):
            if 0 <= r  and r < R and 0 <= c  and c < C and grid[r][c] != 0:
                return True
            else:
                return False

        def maximumGold(r, c):
            deltas = [
                [0,-1],
                [1, 0],
                [0, 1],
                [-1,0]
            ]

            collected = 0
            visited.add((r,c))
            for d in deltas:
                nr, nc = r + d[0], c + d[1]
                if (nr,nc) not in visited and allowed_cell(nr,nc):
                    #print("visited {}".format((nr,nc)))
                    collected = max(collected, maximumGold(nr,nc))
            visited.remove((r,c))  

            return collected + grid[r][c]
        
        max_collected = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 0:
                    max_collected = max(max_collected, maximumGold(r,c))
                    print(r,c, max_collected)
        
        return max_collected


if __name__ == "__main__":
    solution = Solution()

    input_par = [
            [0,6,0],
            [5,8,7],
            [0,9,0]
    ]
    expected_par = 24
    output_par  = solution.getMaximumGold(input_par)
    unittest.TestCase().assertEqual(output_par, expected_par)
    
