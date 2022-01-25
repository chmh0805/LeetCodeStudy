# Solve With String Slice

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)  # filter with regex

        return s == s[::-1]  # slicing


if __name__ == '__main__':
    print(Solution.isPalindrome(Solution, "A man, a plan, a canal: Panama"))
    print(Solution.isPalindrome(Solution, "race a car"))
