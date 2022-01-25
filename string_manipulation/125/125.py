# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = True
        filtered_origin = ''.join(w.lower() for w in s if w.isalnum())
        left_idx, right_idx = 0, len(filtered_origin) - 1
        while left_idx < right_idx:
            if filtered_origin[left_idx] != filtered_origin[right_idx]:
                res = False
                break
            left_idx += 1
            right_idx -= 1
        return res


if __name__ == '__main__':
    print(Solution.isPalindrome(Solution, "A man, a plan, a canal: Panama"))
    print(Solution.isPalindrome(Solution, "race a car"))
