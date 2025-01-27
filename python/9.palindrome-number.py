class Solution:
    """
    approch(my-first)
    """

    # def isPalindrome(self, x: int) -> bool:
    #     x = [i for i in str(x)]
    #     if len(x) % 2 == 0:
    #         center = int(len(x) / 2)
    #         left = x[0:center]
    #         right = x[center : len(x)][::-1]
    #         for i in range(len(left)):
    #             if left[i] != right[i]:
    #                 return False
    #     else:
    #         center = int(len(x) // 2)
    #         left = x[0 : center + 1]
    #         right = x[center : len(x) + 1][::-1]
    #         for i in range(len(left)):
    #             if left[i] != right[i]:
    #                 return False
    #     return True

    """
    approch(Revert half of the number)
    """

    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # As discussed above, when x < 0, x is not a palindrome.
        # Also if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10

        return x == revertedNumber or x == revertedNumber // 10


def test_solution():
    solution = Solution()

    test_cases = [
        {"nums": 121, "expected": True},
        {"nums": -121, "expected": False},
        {"nums": 10, "expected": False},
        {"nums": 0, "expected": True},
        {"nums": 12321, "expected": True},
    ]

    for i, test in enumerate(test_cases):
        result = solution.isPalindrome(test["nums"])
        print(f"Test {i + 1}:")
        print(f"Input: nums = {test['nums']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Pass: {result == test['expected']}\n")


if __name__ == "__main__":
    test_solution()
