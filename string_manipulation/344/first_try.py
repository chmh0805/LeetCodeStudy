from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_idx = 0
        right_idx = len(s) - 1

        while (left_idx < right_idx):
            left_tmp, right_tmp = s[left_idx], s[right_idx]
            del s[left_idx]
            s.insert(left_idx, right_tmp)
            del s[right_idx]
            s.insert(right_idx, left_tmp)
            left_idx += 1
            right_idx -= 1


if (__name__ == '__main__'):
    input_1 = ["h", "e", "l", "l", "o"]
    Solution.reverseString(Solution, input_1)
    print(input_1)

    input_2 = ["H", "a", "n", "n", "a", "h"]
    Solution.reverseString(Solution, input_2)
    print(input_2)
