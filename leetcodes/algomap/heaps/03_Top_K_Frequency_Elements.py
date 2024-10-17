"""
https://leetcode.com/problems/top-k-frequent-elements/
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter


class Solution:
    """
    Solution #1:
    Time Complexity: O(n) - probably, not sure how efficient Counter.most_common() is
    Space Complexity: O(n)

    Solution #2:
    Time: O(n log k), Space: O(k)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        # Solution #1
        # return [x[0] for x in counter.most_common(k)]

        # Solution #2
        heap = []
        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        return [h[1] for h in heap]

