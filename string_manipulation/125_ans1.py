# Solve With List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = True
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                res = False
                break
        return res


if __name__ == '__main__':
    print(Solution.isPalindrome(Solution, "A man, a plan, a canal: Panama"))
    print(Solution.isPalindrome(Solution, "race a car"))
