"""
Example 1:
Input: zero = 1, one = 1, limit = 2
Output: 2
Explanation:
The two possible stable binary arrays are [1,0] and [0,1], as both arrays have a single 0 and a single 1, and no subarray has a length greater than 2.
Example 2:
Input: zero = 1, one = 2, limit = 1
Output: 1
Explanation:
The only possible stable binary array is [1,0,1].
Note that the binary arrays [1,1,0] and [0,1,1] have subarrays of length 2 with identical elements, hence, they are not stable.
Example 3:
Input: zero = 3, one = 3, limit = 2
Output: 14
Explanation:
All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1], [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0], [1,0,1,1,0,0], [1,1,0,0,1,0], and [1,1,0,1,0,0]
"""
import tracemalloc
from unittest import TestCase

def get_memory_usage():
    current, _ = tracemalloc.get_traced_memory()
    return current


class Solution:
    """
    You are given 3 positive integers zero, one, and limit.

    A binary array arr is called stable if:

    The number of occurrences of 0 in arr is exactly zero.
    The number of occurrences of 1 in arr is exactly one.

    Each subarray of arr with a size greater than limit must contain both 0 and 1.
    Return the total number of stable binary arrays.

    Since the answer may be very large, return it modulo 109 + 7.
    """
    """
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

        memo = {}

        ozero = zero
        oone = one
        def dp(zero, one):
            print(zero, one)
            if zero == 0 and one == 0:
                return 1

            if (zero, one) in memo:
                return memo[(zero,one)]

            with_zero = 0
            with_one = 0
            # taking 0 if the lef
            if zero > 0 and abs(zero - one) <= limit and abs(ozero - zero - (oone - one)) <= limit:
                print('taking 0')

                with_zero = dp(zero-1, one)
            if one > 0 and abs(zero - one) <= limit and abs(ozero - zero - (oone - one)) <= limit:
                print('taking 1')
                with_one = dp(zero, one-1)
            
            memo[(zero,one)] = (with_zero + with_one)% (10**9 +7)
            print("in memo",zero, one, memo[(zero,one)])
            return memo[(zero,one)]

        return dp(zero, one)
    """

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        # Memoization cache
        memo = {}

        def dp(zero, one, last_char, streak):
            # Base case: all zeros and ones are used
            if zero == 0 and one == 0:
                return 1

            # Check if the result is already computed
            if (zero, one, last_char, streak) in memo:
                return memo[(zero, one, last_char, streak)]

            total = 0

            # Try adding a 0
            if zero > 0:
                if last_char == 0:
                    if streak < limit:
                        total += dp(zero - 1, one, 0, streak + 1)
                else:
                    total += dp(zero - 1, one, 0, 1)
                total %= MOD

            # Try adding a 1
            if one > 0:
                if last_char == 1:
                    if streak < limit:
                        total += dp(zero, one - 1, 1, streak + 1)
                else:
                    total += dp(zero, one - 1, 1, 1)
                total %= MOD

            # Store the result in the memoization cache
            memo[(zero, one, last_char, streak)] = total
            return total

        # Start the DP with no last character and streak 0
        return dp(zero, one, -1, 0)


if __name__ == "__main__":
    print("Testcase 1")
    test_case_1 = {'input': {'zero': 1, 'one': 1, 'limit': 2},  'expected': 2}
    output = Solution().numberOfStableArrays(**test_case_1['input'])
    TestCase().assertEqual(output, test_case_1['expected'])

    print("Testcase 2")
    test_case_2 = {'input': {'zero': 1, 'one': 2, 'limit': 1},  'expected': 1}
    output = Solution().numberOfStableArrays(**test_case_2['input'])
    TestCase().assertEqual(output, test_case_2['expected'])

    print("Testcase 3")
    test_case_3 = {'input': {'zero': 3, 'one': 3, 'limit': 2},  'expected': 14}
    output = Solution().numberOfStableArrays(**test_case_3['input'])
    TestCase().assertEqual(output, test_case_3['expected'])

    tracemalloc.start()
    initial_memory = get_memory_usage()
    print(f"Initial memory usage: {initial_memory} bytes")
    print("Testcase 4")
    test_case_4 = {'input': {'zero': 55, 'one': 58, 'limit': 31},  'expected': 14}
    output = Solution().numberOfStableArrays(**test_case_4['input'])
    #TestCase().assertEqual(output, test_case_4['expected'])
    snapshot = tracemalloc.take_snapshot()
    final_memory = get_memory_usage()
    print(f"Final memory usage: {final_memory} bytes")
    print(f"Memory used: {(final_memory - initial_memory)/(2**20)} MB")
    tracemalloc.stop()
    print(snapshot.statistics('traceback'))
    for stat in snapshot.statistics('traceback')[:10]:
        print(stat)
