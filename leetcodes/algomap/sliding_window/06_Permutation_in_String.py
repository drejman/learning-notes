"""
https://leetcode.com/problems/permutation-in-string/
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    """
    Solution:
        - get counts of all characters in s1 (as order doesn't matter in this problem)
        - slide windows of the length(s1) (permutation has the same length as original string) over s2, keeping track of updated counts of characters
        - if counts of s1 and window on s2 match then return True
        - if no match occured then return False
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        offset = ord('a')  # value of 'a'

        if len(s1) > len(s2):  # no solution possible
            return False

        counts_s1 = [0] * 26
        counts_s2 = [0] * 26
        n1, n2 = len(s1), len(s2)
        for i in range(n1):
            counts_s1[ord(s1[i]) - offset] += 1
            counts_s2[ord(s2[i]) - offset] += 1

        if counts_s1 == counts_s2:
            return True

        for i in range(n1, n2):
            counts_s2[ord(s2[i]) - offset] += 1
            counts_s2[ord(s2[i - n1]) - offset] -= 1
            if counts_s1 == counts_s2:
                return True

        return False
