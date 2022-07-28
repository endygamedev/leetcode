# Link: https://leetcode.com/problems/search-a-2d-matrix

# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []

        for row in matrix:
            arr = Solution.merge(arr, row)

        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high)//2

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                high -= 1
            else:
                low += 1


    @staticmethod
    def merge(arr1: List[int], arr2: List[int]) -> List[int]:
        res = []

        left, right = 0, 0

        while left < len(arr1) and right < len(arr2):
            if arr1[left] < arr2[right]:
                res.append(arr1[left])
                left += 1
            else:
                res.append(arr2[right])
                right += 1

        while left < len(arr1):
            res.append(arr1[left])
            left += 1

        while right < len(arr2):
            res.append(arr2[right])
            right += 1

        return res
