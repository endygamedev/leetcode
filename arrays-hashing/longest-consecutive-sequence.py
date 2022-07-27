# Link: https://leetcode.com/problems/longest-consecutive-sequence

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        sorted_nums = sorted(nums)
        res, max_res = 1, 1

        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] + 1 == sorted_nums[i + 1]:
                res += 1
            elif sorted_nums[i] == sorted_nums[i + 1]:
                continue
            else:
                max_res = max(res, max_res)
                res = 1

        return max(res, max_res)
