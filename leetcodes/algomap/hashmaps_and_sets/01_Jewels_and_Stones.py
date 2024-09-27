"""
https://leetcode.com/problems/jewels-and-stones/
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

Constraints:
1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Input: jewels - unique list of characters to keep count, stones - list to get counts from
        Output: count of jewels in stones
        Solution:
            iterate through stones
            for each check if is in jewels
            -> check is important, set.isin() should be O(1)
            if yes then increment counter
            time: O(n+m) (if checking in O(1))
            space: O(m)
        """
        count = 0
        jewels = set(jewels)  # for short string searching in string might be faster, also maybe sort string and bisect?
        for stone in stones:
            if stone in jewels:
                count += 1
        return count

        # from collections import Counter
        # counter = Counter(stones)
        # return sum(v for k, v in counter.items() if k in jewels)
