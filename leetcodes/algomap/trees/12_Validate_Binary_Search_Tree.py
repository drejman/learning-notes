"""
https://leetcode.com/problems/validate-binary-search-tree/
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    To validate Binary Search Tree minimum and maximum acceptable values are needed (in case it's a subtree).
    - compare that value of the root is between left and right
    - validate left subtree with maximum value set to value of the root
    - validate right subtree with minimum value set to value of the root
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_BST(root: Optional[TreeNode], min_: int, max_: int) -> bool:
            if root is None:
                return True

            if not (min_ < root.val < max_):
                return False

            return (is_valid_BST(root=root.left, min_=min_, max_=root.val)
                    and is_valid_BST(root=root.right, min_=root.val, max_=max_))

        return is_valid_BST(root=root, min_=-(2 ** 31) - 1, max_=2 ** 31)
