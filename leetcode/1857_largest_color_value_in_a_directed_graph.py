from typing import List
from unittest import TestCase


class Solution:
    """
    There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
    You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.
    A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
    Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

    Example 1:
    Input: colors = abaca, edges = [[0,1],[0,2],[2,3],[3,4]]
    Output: 3
    Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored a (red in the above image).

    Example 2:
    Input: colors = a, edges = [[0,0]]
    Output: -1
    Explanation: There is a cycle from 0 to 0.

    Constraints:
    n == colors.length
    m == edges.length
    1 <= n <= 105
    0 <= m <= 105
    colors consists of lowercase English letters.
    0 <= aj, bj< n
    """
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        C = len(colors)
        g = [ list() for _ in range(C)]

        res = 0
        visited, path = set(), set()
        count = [[0]*26 for _ in range(C)]
        for e in edges:
            g[e[0]].append(e[1])
            
        def dfs(node):
            # return max feq of color
            if node in path:
                return float("inf")
            if node in visited:
                return 0

            visited.add(node)
            path.add(node)
            color_index = ord(colors[node]) - ord('a')
            count[node][color_index] = 1
            

            
            for nei in g[node]:
                if dfs(nei) == float("inf"):
                    return float("inf")

                for c in range(26):
                    
                    count[node][c] = max(
                        count[node][c],
                        ( 1 if c == color_index else 0) + count[nei][c]
                    )
            path.remove(node)
            return max(count[node])

        for i in range(C):
            res = max(dfs(i), res)
        
        return -1 if res == float("inf") else res
            
        
        
             
        
            
        


if __name__ == "__main__":

    # Input: colors = abaca, edges = [[0,1],[0,2],[2,3],[3,4]]
    test_case = {'input': {'colors': "abaca", 'edges': [[0,1],[0,2],[2,3],[3,4]]},  'expected': 3}
    output = Solution().largestPathValue(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

