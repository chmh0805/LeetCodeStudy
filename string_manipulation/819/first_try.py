import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in (
            re.sub('[^\w]', ' ', paragraph).lower().split()
        ) if word not in banned]
        most_common_count = -1
        result = ''

        for word in words:
            if words.count(word) > most_common_count:
                most_common_count = words.count(word)
                result = word

        return result


if __name__ == '__main__':
    output_1 = Solution.mostCommonWord(
        Solution,
        paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
        banned=["hit"])
    print(output_1)  # "ball"

    output_2 = Solution.mostCommonWord(Solution, paragraph="a.", banned=[])
    print(output_2)  # "a"

    output_3 = Solution.mostCommonWord(
        Solution, paragraph="a, a, a, a, b,b,b,c, c", banned=["a"])
    print(output_3)  # "b"
