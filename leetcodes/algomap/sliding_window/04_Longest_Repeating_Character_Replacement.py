"""
https://leetcode.com/problems/longest-repeating-character-replacement/
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string
and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""


class Solution:
    """
    Solution:
    - check all possible positions of the right end of the substring
    - move left end only when it must be moved, i.e. condition is not met
        condition: number of chars other than most common char in the substring <= k
    - keep track of counts of all chars between left and right
      (update each time left or right is moved)
    Time: O(n)
    Space: O(1)
    """

    def characterReplacement(self, s: str, k: int) -> int:
        def get_position(point: int) -> int:
            offset = 65  # value of 'A'
            return ord(s[point]) - offset

        longest = 0
        l = 0
        counts = [0] * 26

        for r in range(len(s)):
            counts[get_position(r)] += 1
            while (r - l + 1) - max(counts) > k:  # move l as long as condition for correct substring is not satisfied
                counts[get_position(l)] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
