"""
https://leetcode.com/problems/valid-perfect-square/description/
367. Valid Perfect Square
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer.
In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

Constraints:
1 <= num <= 2^31 - 1
"""

class Solution:
    """
    Binary search between squares of 1 and the smallest between 2^16 and given number,
    no modifications to the algorithm.
    """
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, min(2**16, num)
        while l <= r:
            m = (l + r) // 2
            sq = m**2
            if sq == num:
                return True
            elif num < sq:
                r = m - 1
            else:
                l = m + 1
        return False
