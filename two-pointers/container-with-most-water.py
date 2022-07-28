# Link: https://leetcode.com/problems/container-with-most-water/

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_ = (right-left)*min(height[left], height[right])

        while left < right:
            val = (right-left)*min(height[left], height[right])
            max_ = max(max_, val)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_
