from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def find_difference(self, s: str, t: str) -> str:
        h1 = {x: 0 for x in s}
        for x in s:
            h1[x] += 1

        h2 = {x: 0 for x in t}
        for x in t:
            h2[x] += 1

        for k, v in h2.items():
            if h1.get(k) != v:
                return k

    def minimum_sum(self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        nums.sort()
        return nums[0]*10 + nums[1]*10 + nums[2] + nums[3]

    def detect_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            slow, fast = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    slow = head
                    while slow != fast:
                        fast = fast.next
                        slow = slow.next
                    return slow
        return None
