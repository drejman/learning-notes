"""
https://leetcode.com/problems/roman-to-integer/description/
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """
            Input: string representing roman numeral
            Output: integer of the same numerical value
            Solution:
                check character and the next one
                if current is the same or bigger than the next one, add to current total and move to next
                if smaller then take next character, subtract current, add to total and move to one after next char
                finish at second to last character
                check if we moved to after the last or not (if the latter then add last char)


            Example:
                MDMXCIV
                M DM XC IV
                in general symbols are ordered from the biggest to smallest,
                i.e. MMDCCCLXXXVIII
                if smaller character is before bigger then it means they form a pair (subtract first symbol from the second and move on)
        """
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        p, l = 0, len(s)
        total = 0

        while p < l - 1:
            current = mapping[s[p]]
            next_ = mapping[s[p + 1]]

            # normal step, add value of a symbol and continue
            if current >= next_:
                total += current
                p += 1

            # take group of two characters, first one is decreasing
            #   the value of the next
            else:
                total += (next_ - current)
                p += 2

        # iteration might end one symbol too early, check
        if p == l - 1:
            total += mapping[s[p]]

        return total
