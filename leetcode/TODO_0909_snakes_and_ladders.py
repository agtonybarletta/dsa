from collections import defaultdict, deque
from typing import List
from unittest import TestCase


class Solution:
    """
    You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.

A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.

Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

 

Example 1:

Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.


Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1


 

Constraints:

n == board.length == board[i].length
2 <= n <= 20
board[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 are not the starting points of any snake or ladder.
    """
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        g = defaultdict(list)
        N = len(board)

        direction = +1
        start = 0
        end = N
        count = 0
        for i in range(N-1, -1, -1):
            for j in range(start, end, direction):
                # do for k in 6
                
                dest = count + k if board != -1 else board
                """
                if board[i][j] != -1:
                    g[count].append((board[i][j]-1, 0))
                else:
                    g[count].extend([(j, 1) for k in range(count+1, count+7) if j < N**2])
                count += 1
                """
            
            if direction == -1:
                start = 0                
                end = N
            else:
                start = N-1
                end = -1
            direction *= -1
        
        dist = [float("inf") for _ in range(N**2)]
        q = deque([0])
        dist[0] = 0
        visited = set()
        while q:
            visiting = q.popleft()
            for n, w in g[visiting]:
                if dist[n] >= dist[visiting] + w:
                    dist[n] = dist[visiting] + w
                if n not in visited:
                    q.append(n)
            visited.add(visiting)
        
        return dist[(N**2)-1] if dist[(N**2)-1] != float("inf") else -1




if __name__ == "__main__":

    # Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    # Output: 4
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    test_case = {'input': {'board': board},  'expected': 4}
    output = Solution().snakesAndLadders(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])


    board = [[1,1,-1],[1,1,1],[-1,1,1]]
    test_case = {'input': {'board': board},  'expected': -1}
    output = Solution().snakesAndLadders(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    board = [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]
    test_case = {'input': {'board': board},  'expected': 2}
    output = Solution().snakesAndLadders(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

    board = [[-1,-1,30,14,15,-1],[23,9,-1,-1,-1,9],[12,5,7,24,-1,30],[10,-1,-1,-1,25,17],[32,-1,28,-1,-1,32],[-1,-1,23,-1,13,19]] 
    test_case = {'input': {'board': board},  'expected': 2}
    output = Solution().snakesAndLadders(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])
