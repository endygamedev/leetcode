# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            val = numbers[left] + numbers[right]
            if val > target:
                right -= 1
            elif val < target:
                left += 1
            else:
                return [left+1, right+1]
