"""
https://leetcode.com/problems/copy-list-with-random-pointer/
A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that
the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y,
then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    """
    Solution:
        traverse the list two times
        first time create new nodes and store them in a hashmap
        second time create new list and fill random nodes with pointers retrieved from hashmap
    """

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        current = head
        old_to_new = {None: None}  # known case that None will stay the same
        while current is not None:
            old_to_new[current] = Node(x=current.val)
            current = current.next

        current = head
        while current is not None:
            node = old_to_new[current]
            node.next = old_to_new[current.next]
            node.random = old_to_new[current.random]
            current = current.next

        return old_to_new[head]
