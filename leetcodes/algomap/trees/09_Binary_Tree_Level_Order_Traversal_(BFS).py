"""
https://leetcode.com/problems/binary-tree-level-order-traversal
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Breadth-First Search:
    - use FIFO queue
    - add root to the queue
    - for each element in the queue (pop left element):
        - add its child nodes to the queue
    Add level order traversal:
    - keep track when starting a level how many nodes it has (length of queue)
    - append all values from the level to one list, that append this list to result
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = [root]
        ans = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            ans.append(level)
        return ans
