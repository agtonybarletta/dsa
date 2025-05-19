from unittest import TestCase
from typing import List, Optional


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        converted = [[0]*n for _ in range(m)]
        NM = len(original)
        print(converted)
        for i in range(NM):
            converted[i // n][i % n] = original[i]

        return converted


if __name__ == "__main__":
    # test_case = {'input': {'original': [1,  2,  3,  4],  'm': 2,  'n': 2},  'expected': [[1, 2], [3, 4]]}
    """
    Input: original = [1,2,3], m = 1, n = 3
    Output: [[1,2,3]]
    """
    test_case = {'input': {'original': [1,  2,  3],  'm': 1,  'n': 3},  'expected': [[1, 2, 3]]}
    output = Solution().construct2DArray(**test_case['input'])

    TestCase().assertEqual(output, test_case['expected'])
