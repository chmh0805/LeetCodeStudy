from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        answer = []
        words = []
        nums = []

        for log in logs:
            if log.split()[1].isdigit():
                nums.append(log)
            else:
                words.append(log)

        words.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        answer = words + nums

        return answer


if __name__ == '__main__':
    input_1 = ["dig1 8 1 5 1", "let1 art can",
               "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(Solution.reorderLogFiles(Solution, input_1))

    input_2 = ["a1 9 2 3 1", "g1 act car",
               "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    print(Solution.reorderLogFiles(Solution, input_2))

    input_3 = ["a1 9 2 3 1", "g1 act car",
               "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]
    print(Solution.reorderLogFiles(Solution, input_3))
