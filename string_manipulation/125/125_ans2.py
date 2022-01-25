# Solve With Deque

import collections
from typing import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = True
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if (strs.popleft() != strs.pop()):
                res = False

        return res


if __name__ == '__main__':
    print(Solution.isPalindrome(Solution, "A man, a plan, a canal: Panama"))
    print(Solution.isPalindrome(Solution, "race a car"))
