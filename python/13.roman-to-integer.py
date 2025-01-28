class Solution:
    """
    approch(my-first)
    """

    # def romanToInt(self, s: str) -> int:
    #     sym_to_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    #     sum = 0
    #     before_sym = ""
    #     for sym in s:
    #         if before_sym == "I":
    #             if sym == "V":
    #                 sum -= sym_to_val[before_sym]
    #                 sum += 4
    #             elif sym == "X":
    #                 sum -= sym_to_val[before_sym]
    #                 sum += 9
    #             else:
    #                 sum += sym_to_val[sym]
    #         elif before_sym == "X":
    #             if sym == "L":
    #                 sum -= sym_to_val[before_sym]
    #                 sum += 40
    #             elif sym == "C":
    #                 sum -= sym_to_val[before_sym]
    #                 sum += 90
    #             else:
    #                 sum += sym_to_val[sym]
    #         elif before_sym == "C":
    #             if sym == "D":
    #                 sum -= sym_to_val[before_sym]
    #                 sum += 400
    #             elif sym == "M":
    #                 sum -= sym_to_val[before_sym]
    #                 sum += 900
    #             else:
    #                 sum += sym_to_val[sym]
    #         else:
    #             sum += sym_to_val[sym]

    #         before_sym = sym
    #     return sum

    """
    approch(Left-to-Right Pass)
    """

    # def romanToInt(self, s: str) -> int:
    #     values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    #     total = 0
    #     i = 0
    #     while i < len(s):
    #         if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
    #             total += values[s[i + 1]] - values[s[i]]
    #             i += 2
    #         else:
    #             total += values[s[i]]
    #             i += 1
    #     return total

    """
    approch(Left-to-Right Pass Improved)
    """

    # def romanToInt(self, s: str) -> int:
    #     values = {
    #         "I": 1,
    #         "V": 5,
    #         "X": 10,
    #         "L": 50,
    #         "C": 100,
    #         "D": 500,
    #         "M": 1000,
    #         "IV": 4,
    #         "IX": 9,
    #         "XL": 40,
    #         "XC": 90,
    #         "CD": 400,
    #         "CM": 900,
    #     }
    #     total = 0
    #     i = 0
    #     while i < len(s):
    #         if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
    #             total += values[s[i : i + 2]]
    #             i += 2
    #         else:
    #             total += values[s[i]]
    #             i += 1

    #     return total

    """
    approch(Right-to-Left Pass)
    """

    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = values[s[-1]]
        for i in reversed(range(len(s) - 1)):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total


def test_solution():
    solution = Solution()

    test_cases = [
        {"input": "III", "expected": 3},
        {"input": "LVIII", "expected": 58},
        {"input": "MCMXCIV", "expected": 1994},
        {"input": "MMCMLXXXIX", "expected": 2989},
    ]

    for i, test in enumerate(test_cases):
        result = solution.romanToInt(test["input"])
        print(f"Test {i + 1}:")
        print(f"Input: {test['input']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Pass: {result == test['expected']}\n")


if __name__ == "__main__":
    test_solution()
