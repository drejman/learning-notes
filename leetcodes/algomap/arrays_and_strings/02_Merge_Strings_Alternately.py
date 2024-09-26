"""
https://leetcode.com/problems/merge-strings-alternately/description/
1768. Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Input: two strings
        Ouput: one string of alternatively merged characters from each string, starting from the first one, then the rest of the longer string.
        Solution:
            two pointers: to current element on words
            if any pointer exceeds length then break
            finish reading from the remaining word
        """

        p1, p2 = 0, 0
        l1, l2 = len(word1), len(word2)
        chars = []

        while p1 < l1 and p2 < l2:
            chars.append(word1[p1])
            p1 += 1
            chars.append(word2[p2])
            p2 += 1

        while p1 < l1:
            chars.append(word1[p1])
            p1 += 1

        while p2 < l2:
            chars.append(word2[p2])
            p2 += 1

        return "".join(chars)

        # Solution:
        #     get length of common part (shorter string)
        #     get string to be appended (slice of longer one)
        #     iterate
        #     append
        # len1, len2 = len(word1), len(word2)
        # len_diff = len1 - len2
        # min_len = len1 - len_diff if len_diff >= 0 else len2 + len_diff
        # end_string = word1[min_len:] if len_diff >= 0 else word2[min_len:]
        # chars = []
        # for i in range(min_len):
        #     chars.append(word1[i])
        #     chars.append(word2[i])
        # return "".join(chars) + end_string

        # oneline solution
        # from itertools import zip_longest
        # return "".join("".join(x) for x in zip_longest(word1, word2, fillvalue=""))
