"""
https://leetcode.com/problems/container-with-most-water/
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        input: list of heights (0+ integers)
        output: area of water
        Area of water is equal to product of the distance between chosen heights
        and the smaller of the two chosen heights.
        In order to maximize this quantity, we want to have highest possible values
        as close to ends as possible.
        Distance is easier to reason about, because it changes uniformly, moving index
        by 1 changes distance by 1. Heights are changing in an unknown pattern.
        Start with area with greatest possible distance: len(height) - 1
        and height: min(height[0], height[-1]).
        To move either left or right height it has to have greater value (because
        it will definetely be closer to the other end), so all smaller or equal values
        can be skipped (because same height and smaller distance, so smaller area).

        How to move pointers
            Start pointer at the ends of list, calculate current best area
            move the pointer with the lower height (the other one won't impact the area)
                if they are the same move left
            exit when left pointer touches right

        Example #1:  [1, 100, 100, 7, 2, 5, 4, 1]
                area = 0, l = 0, r = 7
            1:  area = 7, l = 1, r = 7
            2: area = 7, l = 1, r = 6
            3: area = 24, l = 1, r = 5
            4: area = 25, l = 1, r = 4
            5: area = 25, l = 1, r = 3
            6: area = 25, l = 1, r = 2
            7: area = 100, l = 2, r = 2
            exit
        """

        area = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = max(area, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:  # move smaller height as bigger won't change area
                l += 1
            else:
                r -= 1
        return area
