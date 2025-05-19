from typing import List
from unittest import TestCase


class Solution:
    """
    You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
    The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
    Return the maximum score of a pair of sightseeing spots.
    """
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        """
        # O(n^2)
        max_score = 0
        N = len(values)
        for i in range(0, N-1):
            for j in range(i+1, N):
                score = values[i] + values[j] + i  - j
                max_score = max(score, max_score)

        return max_score
        """
        max_score = 0
        N = len(values)
        best_i_score = [values[0]]
        for i in range(1, N):
            best_i_score.append(max(best_i_score[i-1], values[i]+i))

        print(best_i_score)

        for j in range(1, N):
            print(j, best_i_score[j-1], values[j])
            max_score = max(max_score, best_i_score[j-1] + values[j] - j)
            print(max_score)

        return max_score


if __name__ == "__main__":
    """
    Example 1:

    Input: values = [8,1,5,2,6]
    Output: 11
    Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
    Example 2:

    Input: values = [1,2]
    Output: 2

    """
    print("Testcase 1")
    test_case_1 = {'input': {'values': [8, 1, 5, 2, 6]},  'expected': 11}
    output = Solution().maxScoreSightseeingPair(**test_case_1['input'])
    TestCase().assertEqual(output, test_case_1['expected'])

    print("Testcase 2")
    test_case_2 = {'input': {'values': [1,  2]},  'expected': 2}
    output = Solution().maxScoreSightseeingPair(**test_case_2['input'])
    TestCase().assertEqual(output, test_case_2['expected'])

    print("Testcase 3")
    test_case_2 = {'input': {'values': [2,  2, 2]},  'expected': 3}
    output = Solution().maxScoreSightseeingPair(**test_case_2['input'])
    TestCase().assertEqual(output, test_case_2['expected'])
        