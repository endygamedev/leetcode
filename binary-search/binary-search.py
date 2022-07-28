# Link: https://leetcode.com/problems/binary-search/

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high)//2
            guess = nums[mid]

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high -= 1
            else:
                low += 1

        return -1
