from unittest import TestCase


class Solution:
    """
    You are given a string word.

    Return the maximum number of non-intersecting substrings of word that are at least four characters long and start and end with the same letter.

    A substring is a contiguous non-empty sequence of characters within a string.

    Example 1:

    Input: word = abcdeafdef

    Output: 2

    Explanation:

    The two substrings are abcdea and fdef.

    Example 2:

    Input: word = bcdaaaab

    Output: 1

    Explanation:

    The only substring is aaaa. Note that we cannot also choose bcdaaaab since it intersects with the other substring.

     

    Constraints:

    1 <= word.length <= 2 * 105
    word consists only of lowercase English letters.
    """
    def maxSubstrings(self, word: str) -> int:
        last = [-1] * 26
        N = len(word)
        count = 0

        for i in range(N):
            idx = ord(word[i]) - ord('a')
            if last[idx] == -1:
                last[idx] = i
            elif (i - last[idx] +1) >= 4:
                count += 1
                last = [-1] * N
        return count





if __name__ == "__main__":

    # Input: word = abcdeafdef
    # Output: 2
    test_case = {'input': {'word': "abcdeafdef"},  'expected': 2}
    output = Solution().maxSubstrings(**test_case['input'])
    TestCase().assertEqual(output, test_case['expected'])

