"""
https://leetcode.com/problems/valid-palindrome
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Solution:
            two pointers, initially at the beginning and at the end
            compare if characters are the same and return immediately False if not
            move pointers towards the middle, if character is not alphanumeric move again
            stop if they point to the same or have crossed
            return True
            Time: O(n)
            Space: O(1)
        """
        left, right = 0, len(s) - 1
        while left < right:
            # skip not alphanumeric characters
            while left < len(s) and not s[left].isalnum():
                left += 1
                continue
            while right >= 0 and not s[right].isalnum():
                right -= 1
                continue

            # exit condition if stepped out on non-alphanumeric characters
            if left >= len(s) or right < 0:
                return True

            # compare characters
            if s[left].lower() != s[right].lower():
                return False

            # next step
            left += 1
            right -= 1

        return True
