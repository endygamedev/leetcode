# Link: https://www.lintcode.com/problem/659/

# encode:
#   - Time Complexity: O(n)
#   - Space Complexity: O(1)

# decode:
#   - Time Complexity: O(n^2)
#   - Space Complexity: O(1)


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1:j + 1 + length])
            i = j + 1 + length

        return res
