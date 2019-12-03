# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def buildList(values):
    curr = None
    first = None
    for value in values:
        next = ListNode(value)
        if curr is not None:
            curr.next = next
        curr = next
        if first is None:
            first = curr
    return first


def printList(head):
    if head is not None:
        print(head.val)
        printList(head.next)


testList = buildList([1, 2, 3, 4, 5, 6])
printList(testList)

print("Range test:")
for x in range(0):
    print(x)


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        i = m - 1
        j = n - 1

        curr = None
        next = head
        x = 0
        while x < i:
            x += 1
            curr = next
            next = next.next
        result = before = None
        if i > 0:
            result = head
            before = curr

        tail = next
        while x <= j:
            x += 1
            prev = curr
            curr = next
            next = next.next
            curr.next = prev
        if result is None:
            result = curr
        else:
            before.next = curr
        tail.next = next

        return result


print("After revert:")
printList(Solution().reverseBetween(testList, 2, 5))
