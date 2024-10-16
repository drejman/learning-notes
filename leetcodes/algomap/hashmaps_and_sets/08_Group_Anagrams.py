"""
https://leetcode.com/problems/group-anagrams/
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


class Solution:
    """
    Observation:
    Anagrams have exactly the same frequency of characters.

    Solution:
    Create a dict (hashmap) where keys will be structure containing alphabetically ordered characters and their counts,
    and values will be a list.
    Then for each word calculate characters frequencies, get a correct list from a dict, and append to the list.
    Return in a correct format (list of lists).
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[tuple, list] = defaultdict(list)
        for word in strs:
            counts = defaultdict(int)
            for char in word:
                counts[char] += 1
            char_counts = tuple(sorted(((k, v) for k, v in counts.items()), key=lambda x: x[0]))
            groups[char_counts].append(word)

        return [group for group in groups.values()]
