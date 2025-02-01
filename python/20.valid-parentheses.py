class Solution:
    """
    approch(Stacks)
    """

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 or len(s) == 0:
            return False

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings.
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:
            # If the character is an closing bracket
            if char in mapping:
                # Pop the topmost element from the stack
                # Otherwise assign a dummy value of '#' to the top_element variable
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = "#"

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        return not stack


def test_solution():
    solution = Solution()

    test_cases = [
        {"input": "()", "expected": True},
        {"input": "()[]{}", "expected": True},
        {"input": "(]", "expected": False},
        {"input": "([])", "expected": True},
        {"input": "({)[}]", "expected": False},
        {"input": "){", "expected": False},
    ]

    for i, test in enumerate(test_cases):
        result = solution.isValid(test["input"])
        print(f"Test {i + 1}:")
        print(f"Input: {test['input']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Pass: {result == test['expected']}\n")


if __name__ == "__main__":
    test_solution()
