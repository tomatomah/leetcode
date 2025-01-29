from typing import List


class Solution:
    """
    approch(my-fist)
    """

    # def longestCommonPrefix(self, strs):
    #     prefix = []
    #     for x in zip(*strs):
    #         if len(set(x)) == 1:
    #             prefix.append(x[0])
    #         else:
    #             break
    #     return "".join(prefix)

    """
    approch(Horizontal scanning)
    """

    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if len(strs) == 0:
    #         return ""
    #     prefix = strs[0]
    #     for i in range(1, len(strs)):
    #         while strs[i].find(prefix) != 0:
    #             prefix = prefix[0 : len(prefix) - 1]
    #             if prefix == "":
    #                 return ""
    #     return prefix

    """
    approch(Vertical scanning)
    """

    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if len(strs) == 0:
    #         return ""
    #     for i in range(len(strs[0])):
    #         c = strs[0][i]
    #         for j in range(1, len(strs)):
    #             if i == len(strs[j]) or strs[j][i] != c:
    #                 return strs[0][0:i]
    #     return strs[0]

    """
    approch(Binary search)
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        minlen = min(len(x) for x in strs)
        low, high = 1, minlen
        before_middle = 0
        while low <= high:
            middle = (low + high) // 2
            if self.isCommonPrefix(strs, middle):
                before_middle = middle
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][:before_middle]

    def isCommonPrefix(self, strs, m):
        str1 = strs[0][:m]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True


def test_solution():
    solution = Solution()

    test_cases = [
        {"input": ["flower", "flow", "flight"], "expected": "fl"},
        {"input": ["dog", "racecar", "car"], "expected": ""},
        {"input": ["leets", "leetcode", "leetc", "leeds"], "expected": "lee"},
        {"input": ["a"], "expected": "a"},
        {"input": ["aa"], "expected": "aa"},
    ]

    for i, test in enumerate(test_cases):
        result = solution.longestCommonPrefix(test["input"])
        print(f"Test {i + 1}:")
        print(f"Input: {test['input']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Pass: {result == test['expected']}\n")


if __name__ == "__main__":
    test_solution()
