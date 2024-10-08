"""
https://leetcode.com/problems/merge-two-sorted-lists/
21. Merge two sorted lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Solution:
        keep pointers to two linked lists
        compare heads of two lists
        pick smaller as head of result list
        change list pointer to next
        change next to None
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val >= list2.val:
            head = list2
            list2 = head.next
            head.next = None
        else:
            head = list1
            list1 = head.next
            head.next = None

        current = head
        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                current.next = list2
                current = list2
                list2 = list2.next
                current.next = None
            else:
                current.next = list1
                current = list1
                list1 = list1.next
                current.next = None

        if list1 is not None:
            current.next = list1
        else:
            current.next = list2
        
        return head