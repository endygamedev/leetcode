# Link: https://leetcode.com/problems/valid-anagram/

# Time Complexity: O(nlog(n)) (Quicksort)
# Space Complexity: O(1)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
