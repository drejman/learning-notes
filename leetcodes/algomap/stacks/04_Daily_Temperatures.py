"""
https://leetcode.com/problems/daily-temperatures/description/
739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that
answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
"""


class Solution:
    """
    Solution:
        use stack
        - go from start
        - pop element from stack, compare temperatures, if condition is satisfied update answer and continue with next element, else move back to stack and stop comparing
        (because elements on the stack will be sorted non-increasingly, as increasing values would pop previous elements from the stack)
        - add current temperature and day to the stack
        - fill up any missing with 0s (or initialize at 0)
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for curr_day, curr_temp in enumerate(temperatures):
            while stack:
                record_temp, record_day = stack.pop()
                if  curr_temp > record_temp:
                    answer[record_day] = curr_day - record_day
                else:
                    stack.append((record_temp, record_day))
                    stack.append((curr_temp, curr_day))
                    break
            else:
                stack.append((curr_temp, curr_day))
        return answer
