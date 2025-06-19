from typing import List
from unittest import TestCase


class Solution:
    """
    Print all palindromic numbers of length n characters in base k
    """

    def palindromic(self, n: int, k: int) -> List[str]:
        if k< 1 or k > 36:
            return []

        palindromic_list = []
        alphabet = [ chr(ord('0') + i) for i in range(min(10, k))]
        if k > 10:
            alphabet.extend([ chr(ord('A') + i) for i in range(k-10)])

        # construct single char palindromic
        for c in alphabet:
            palindromic_list.append(c)

        if n == 1:
            return palindromic_list

        # construct single char palindromic
        for c in alphabet:
            palindromic_list.append(c+c)

        for i in range(0, n-2):
            to_append = []
            for p in palindromic_list:
                for c in alphabet:
                    if len(p) +2 <= n:
                        to_append.append(c + p + c)
            palindromic_list.extend(to_append)
        return palindromic_list





if __name__ == "__main__":

    test_case = {'input': {'n': 3, 'k': 2},  'expected': ['0', '1', '00', '11', '000', '010', '111', '101']}
    output = Solution().palindromic(**test_case['input'])
    TestCase().assertEqual(set(output), set(test_case['expected']))

    test_case = {'input': {'n': 2, 'k': 4},  'expected': ['0', '1', '2', '3', '00', '11', '22', '33']}
    output = Solution().palindromic(**test_case['input'])
    TestCase().assertEqual(set(output), set(test_case['expected']))

    test_case = {'input': {'n': 1, 'k': 16},  'expected': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']}
    output = Solution().palindromic(**test_case['input'])
    TestCase().assertEqual(set(output), set(test_case['expected']))


    expected = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', '000', '101', '202', '303', '404', '505', '606', '707', '808', '909', 'A0A', 'B0B', 'C0C', 'D0D', 'E0E', 'F0F', '010', '111', '212', '313', '414', '515', '616', '717', '818', '919', 'A1A', 'B1B', 'C1C', 'D1D', 'E1E', 'F1F', '020', '121', '222', '323', '424', '525', '626', '727', '828', '929', 'A2A', 'B2B', 'C2C', 'D2D', 'E2E', 'F2F', '030', '131', '232', '333', '434', '535', '636', '737', '838', '939', 'A3A', 'B3B', 'C3C', 'D3D', 'E3E', 'F3F', '040', '141', '242', '343', '444', '545', '646', '747', '848', '949', 'A4A', 'B4B', 'C4C', 'D4D', 'E4E', 'F4F', '050', '151', '252', '353', '454', '555', '656', '757', '858', '959', 'A5A', 'B5B', 'C5C', 'D5D', 'E5E', 'F5F', '060', '161', '262', '363', '464', '565', '666', '767', '868', '969', 'A6A', 'B6B', 'C6C', 'D6D', 'E6E', 'F6F', '070', '171', '272', '373', '474', '575', '676', '777', '878', '979', 'A7A', 'B7B', 'C7C', 'D7D', 'E7E', 'F7F', '080', '181', '282', '383', '484', '585', '686', '787', '888', '989', 'A8A', 'B8B', 'C8C', 'D8D', 'E8E', 'F8F', '090', '191', '292', '393', '494', '595', '696', '797', '898', '999', 'A9A', 'B9B', 'C9C', 'D9D', 'E9E', 'F9F', '0A0', '1A1', '2A2', '3A3', '4A4', '5A5', '6A6', '7A7', '8A8', '9A9', 'AAA', 'BAB', 'CAC', 'DAD', 'EAE', 'FAF', '0B0', '1B1', '2B2', '3B3', '4B4', '5B5', '6B6', '7B7', '8B8', '9B9', 'ABA', 'BBB', 'CBC', 'DBD', 'EBE', 'FBF', '0C0', '1C1', '2C2', '3C3', '4C4', '5C5', '6C6', '7C7', '8C8', '9C9', 'ACA', 'BCB', 'CCC', 'DCD', 'ECE', 'FCF', '0D0', '1D1', '2D2', '3D3', '4D4', '5D5', '6D6', '7D7', '8D8', '9D9', 'ADA', 'BDB', 'CDC', 'DDD', 'EDE', 'FDF', '0E0', '1E1', '2E2', '3E3', '4E4', '5E5', '6E6', '7E7', '8E8', '9E9', 'AEA', 'BEB', 'CEC', 'DED', 'EEE', 'FEF', '0F0', '1F1', '2F2', '3F3', '4F4', '5F5', '6F6', '7F7', '8F8', '9F9', 'AFA', 'BFB', 'CFC', 'DFD', 'EFE', 'FFF']
    test_case = {'input': {'n': 3, 'k': 16},  'expected': expected}
    output = Solution().palindromic(**test_case['input'])
    TestCase().assertEqual(set(output), set(test_case['expected']))
