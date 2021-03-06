# Link: https://leetcode.com/problems/two-sum/

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = dict()

        for i, val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[val] = i
        return
