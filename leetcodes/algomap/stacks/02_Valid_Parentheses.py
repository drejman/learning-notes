"""
https://leetcode.com/problems/valid-parentheses/
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""


class Solution:
    """
    Input: string containing "(){}[]" characters
    Output: True if string is a valid set of parentheses; False otherwise
    Solution:
        - need to match closing characters to already open ones
        - need to close most recently opened parenthesis
        If character is opening push to stack
        If character is closing:
        - fail if stack is empty
        - pop from stack, compare characters, if brackets are the same type continue,
          else fail
        Return True if stack is empty
        Time: O(n)
        Space: O(n)
    """

    def isValid(self, s: str) -> bool:
        closing = "}])"
        matching = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        stack = []
        for char in s:
            if char in closing:
                if not stack:
                    return False
                if matching[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return not stack
