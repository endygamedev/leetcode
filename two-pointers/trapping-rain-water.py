# Link: https://leetcode.com/problems/trapping-rain-water

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]

        return res
