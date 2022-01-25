# Swap With Two Pointers

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_idx, right_idx = 0, len(s) - 1
        while left_idx < right_idx:
            s[left_idx], s[right_idx] = s[right_idx], s[left_idx]
            left_idx += 1
            right_idx -= 1


if (__name__ == '__main__'):
    input_1 = ["h", "e", "l", "l", "o"]
    Solution.reverseString(Solution, input_1)
    print(input_1)

    input_2 = ["H", "a", "n", "n", "a", "h"]
    Solution.reverseString(Solution, input_2)
    print(input_2)
