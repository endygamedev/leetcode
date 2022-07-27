# Link: https://leetcode.com/problems/contains-duplicate/

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
