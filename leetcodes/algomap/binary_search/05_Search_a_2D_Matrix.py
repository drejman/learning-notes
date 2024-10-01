"""
https://leetcode.com/problems/search-a-2d-matrix/submissions/1407474499/
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        input: 2D matrix, target value to be searched
        output: bool (true if target in matrix else false)
        Solution:
            first find in each row the value would be
            either look at first element or the last element of each row
                - binary search O(log m)
            then search the selected row for target value
                - binary search O(log n)
            log(m) + log(n) = log(m*n)

        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
        #1: last element comparison
            1:  s = 0, e = 2, m = 1
                el = 20 > target
                e = 1 - 1 = 0
            2:  s = 0, e = 0, m = 0
                el = 7 < target
                s = 0 + 1 = 1
            exit loop
            target element is definetely between end of row 0 and end of row 1
            in row 1 -> in row[s]
        #2: first element comparison
            1:  s = 0, e = 2, m = 1
                el = 10 < target
                s = 1 + 1 = 2
            2:  s = 2, e = 2, m = 2
                el = 23 > target
                e = 2 - 1 = 1
            exit loop
            target element is definetely between start of row 1 and start of row 2
            in row 1 -> in row[e]

        """
        start, end = 0, len(matrix) - 1

        # Start of solution #1, comparing ends of rows
        while start <= end:
            mid = (start + end) // 2
            elem = matrix[mid][-1]
            if elem == target:
                return True
            elif elem < target:
                start = mid + 1
            else:
                end = mid - 1

        if start >= len(matrix):
            return False
        nums = matrix[start]
        # end of #1

        # Start of solution #2, comparing begginings of row
        # while start <= end:
        #     mid = (start + end) // 2
        #     elem = matrix[mid][0]
        #     if elem == target:
        #         return True
        #     elif elem < target:
        #         start = mid + 1
        #     else:
        #         end = mid - 1

        # print(end)
        # if end < 0:
        #     return False
        # nums = matrix[end]
        # End of #2

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False
