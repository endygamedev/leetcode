# Link: https://leetcode.com/problems/valid-palindrome/

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_s = [ch.lower() for ch in s if ch.isalpha() or ch.isdigit()]
        return list(reversed(valid_s)) == valid_s
