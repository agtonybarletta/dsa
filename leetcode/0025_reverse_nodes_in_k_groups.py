from typing import Optional
from unittest import TestCase
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        s = ""
        head = self
        while head != None:
            s += str(head.val) + ", "
            head = head.next
        return s


class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:
        dummyHead = ListNode(-1, None)

        writing = dummyHead
        reading = head
        counting = head
        counted = 0
        while counting != None:
            if counted > 0 and counted % k == 0:
                while reading != counting:
                    tmp = writing.next
                    writing.next = ListNode(reading.val, tmp)
                    reading = reading.next
                while writing.next != None:
                    writing = writing.next
            counting = counting.next
            counted += 1
        writing.next = reading
        return dummyHead.next
                    
if __name__ == "__main__":
    
    get_list_node = lambda a: None if len(a) == 0 else ListNode(a[0], get_list_node(a[1:]))
    array = [1, 2, 3, 4, 5]
    l = get_list_node(array)
    k = 2
    # check
    get_array = lambda l: [] if l == None else [l.val] + get_array(l.next)
    output_list = Solution().reverseKGroup(l, k)
    output = get_array(output_list)
    expected = [2, 1, 4, 3, 5]

    TestCase().assertEqual(output, expected)


