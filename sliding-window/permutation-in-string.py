# Link: https://leetcode.com/problems/permutation-in-string

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = dict(), dict()

        # O(26) ~ O(1)
        for i in range(ord('a'), ord('z') + 1):
            s1_count[chr(i)] = 0
            s2_count[chr(i)] = 0

        # O(n1)
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1

        # O(n2-n1) ~ O(n)
        for i in range(len(s2)-len(s1)):
            if s1_count == s2_count:
                return True

            s2_count[s2[i + len(s1)]] += 1
            s2_count[s2[i]] -= 1

        return s1_count == s2_count
