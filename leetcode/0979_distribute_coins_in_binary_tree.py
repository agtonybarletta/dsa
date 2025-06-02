"""
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

Example 1:


Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:


Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.
 

Constraints:

The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
import typing as ty
import unittest as ut


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: ty.Optional[TreeNode]) -> int:

        def traverse(node):
            if node is None:
                return 0, 0

            l_net_coin, l_moves = traverse(node.left)
            r_net_coin, r_moves = traverse(node.right)

            net_coin = node.val + l_net_coin + r_net_coin - 1
            moves = l_moves + r_moves + abs(net_coin)
            return net_coin, moves

        return traverse(root)[1]


if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(3, TreeNode(0), TreeNode(0))
    expected_par = 2
    output_par = solution.distributeCoins(root)
    ut.TestCase().assertEqual(output_par, expected_par)

    root = TreeNode(0, TreeNode(3), TreeNode(0))
    expected_par = 3
    output_par = solution.distributeCoins(root)
    ut.TestCase().assertEqual(output_par, expected_par)
