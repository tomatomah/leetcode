from typing import List


class Solution:
    """
    approch1(Brute Force)
    """

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         x = target - nums[i]
    #         for j in range(i + 1, len(nums)):
    #             if x == nums[j]:
    #                 return [i, j]
    #     return []

    """
    approch2(Two-pass Hash Table)
    """

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hashmap = {}
    #     for i in range(len(nums)):
    #         hashmap[nums[i]] = i
    #     for i in range(len(nums)):
    #         complement = target - nums[i]
    #         if complement in hashmap and hashmap[complement] != i:
    #             return [i, hashmap[complement]]
    #     return []

    """
    approch3(One-pass Hash Table)
    """

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hashmap = {}
    #     for i in range(len(nums)):
    #         complement = target - nums[i]
    #         if complement in hashmap:
    #             return [i, hashmap[complement]]
    #         hashmap[nums[i]] = i
    #     return []

    """
    approch4(Custom)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []


def test_solution():
    solution = Solution()

    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
    ]

    for i, test in enumerate(test_cases):
        result = solution.twoSum(test["nums"], test["target"])
        print(f"Test {i + 1}:")
        print(f"Input: nums = {test['nums']}, target = {test['target']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Pass: {sorted(result) == sorted(test['expected'])}\n")


if __name__ == "__main__":
    test_solution()
