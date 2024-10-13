"""
https://leetcode.com/problems/first-bad-version/
278. First Bad Version
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.


Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 2^31 - 1
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    """
    Modified binary search until it gets to just one value.
    Normally binary search exits loop while pointers cross (all values have been checked)
    or inspected value is equal to the target.
    Here the need is to stop at the first value from the sequence of the same values, so modifications are:
    - always return result (it's not possible to not find a result)
    - exit when pointers are at the same value -> must be the answer
    - as the value we are looking for is on the right side of the interval, move right pointer to exactly mid position
    (i.e. right pointer should always point to the searched value); left can be moved to the next value (as usual)
    """
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l < r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l

