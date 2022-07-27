# Link: https://leetcode.com/problems/group-anagrams/

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = dict()
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp not in dict_.keys():
                dict_[tmp] = []
            dict_[tmp].append(s)
        return dict_.values()
