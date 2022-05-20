from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        if len(strs) == 1:
            return [strs]

        for str in strs:
            if anagrams.get(''.join(sorted(str))) == None:
                anagrams[''.join(sorted(str))] = []
            anagrams[''.join(sorted(str))].append(str)

        return list(anagrams.values())


if __name__ == '__main__':
    output_1 = Solution.groupAnagrams(
        Solution,
        strs=["eat", "tea", "tan", "ate", "nat", "bat"]
    )
    print(output_1)  # [["bat"],["nat","tan"],["ate","eat","tea"]]

    output_2 = Solution.groupAnagrams(Solution, strs=[""])
    print(output_2)  # [[""]]

    output_3 = Solution.groupAnagrams(
        Solution, strs=["a"])
    print(output_3)  # [["a"]]
