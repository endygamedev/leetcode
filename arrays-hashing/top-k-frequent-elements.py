# Link: https://leetcode.com/problems/top-k-frequent-elements/

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = dict()

        for num in nums:
            if num not in dict_.keys():
                dict_[num] = 0
            dict_[num] += 1

        soreted_dict = dict(sorted(dict_.items(), key=lambda item: -item[1]))

        return list(soreted_dict.keys())[:k]
