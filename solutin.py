class ListNode:
    def __init__(sefl, val: int | float):
        self.val: int | float = val
        self.next: ListNode = None


class Stack:
    def __init__(self) -> None:
        self._items: list[int | float] = []

    def push(self, val) -> None:
        self._items.append(val)

    def pop(self) -> int | float:
        if not self.is_empty():
            return self._items.pop()
        return None

    def is_empty(self) -> bool:
        return not self._items

    def peek(self) -> int | float | None:
        if not self.is_empty():
            return self._items[-1]
        return None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode | None:

    if headA == None or headB == None:
        return None

    pointerA: ListNode = headA
    pointerB: ListNode = headB

    while pointerA != pointerB:
        if pointerA != None:
            pointerA = pointerA.next
        else:
            pointera = headB
        if pointerB != None:
            pointerB = pointerB.next
        else:
            pointerB = headA
    return pointerA


def sort_stack(original_stack) -> Stack:
    temp_stack: Stack = Stack()

    while not original_stack.is_empty():
        temp: float | int = original_stack.pop()

        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            original_stack.push(temp_stack.pop())
        temp_stack.push(temp)

    while not temp_stack.is_empty():
        original_stack.push(temp_stack.pop())

    return original_stack


def run_tests():
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)

    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common

    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = common

    assert getIntersectionNode(headA, headB) == common

    A2 = ListNode(1)
    A2.next = ListNode(2)
    B2 = ListNode(3)
    B2.next = ListNode(4)
    assert getIntersectionNode(A2, B2) == None

    assert getIntersectionNode(headA, None) == None

    print("Тесты списков пройдены")

    def stack_to_list(s):
        res = []
        while not s.is_empty():
            res.append(s.pop())
        return res

    s1 = Stack()
    for val in [5, 2, 8, 1, 3]:
        s1.push(val)
    sort_stack(s1)
    assert stack_to_list(s1) == [1, 2, 3, 5, 8]

    s2 = Stack()
    for val in [10, 5, 2]:
        s2.push(val)
    sort_stack(s2)
    assert stack_to_list(s2) == [
        2,
        5,
        10,
    ]

    s3 = Stack()
    sort_stack(s3)
    assert stack_to_list(s3) == []

    s4 = Stack()
    for val in [3, 3, 1, 1]:
        s4.push(val)
    sort_stack(s4)
    assert stack_to_list(s4) == [1, 1, 3, 3]

    print("Тесты стека пройдены")


if __name__ == "__main__":
    run_tests()
