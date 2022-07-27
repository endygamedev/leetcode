# Link: https://leetcode.com/problems/3sum

# Time Complexity: O(n^2)
# Space Complexity: O(1)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)

        for i, val in enumerate(sorted_nums):
            if i > 0 and val == sorted_nums[i-1]:
                continue

            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                sum_ = val + sorted_nums[left] + sorted_nums[right]
                if sum_ > 0:
                    right -= 1
                elif sum_ < 0:
                    left += 1
                else:
                    res.append([val, sorted_nums[left], sorted_nums[right]])
                    left += 1
                    while sorted_nums[left] == sorted_nums[left-1] and left < right:
                        left += 1

        return res
