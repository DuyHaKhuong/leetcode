"""
LeetCode: Design Circular Deque
URL: https://leetcode.com/problems/design-circular-deque/
Difficulty: Medium
Fetched: 2025-10-05 18:07:40

Description:
Design and implement a circular double-ended queue (deque).

Implement the class MyCircularDeque with the following operations:
- MyCircularDeque(k): Initialize the deque with maximum size k.
- insertFront(value): Add an item at the front; return true if successful, false otherwise.
- insertLast(value): Add an item at the rear; return true if successful, false otherwise.
- deleteFront(): Delete an item from the front; return true if successful, false otherwise.
- deleteLast(): Delete an item from the rear; return true if successful, false otherwise.
- getFront(): Return the front item; return -1 if the deque is empty.
- getRear(): Return the last item; return -1 if the deque is empty.
- isEmpty(): Return true if the deque is empty, false otherwise.
- isFull(): Return true if the deque is full, false otherwise.

Examples:
- Example 1
  Input:
    ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
    [[3], [1], [2], [3], [4], [], [], [], [4], []]
  Output:
    [null, true, true, true, false, 2, true, true, true, 4]
  Explanation:
    MyCircularDeque myCircularDeque = new MyCircularDeque(3);
    myCircularDeque.insertLast(1);  // return true
    myCircularDeque.insertLast(2);  // return true
    myCircularDeque.insertFront(3); // return true
    myCircularDeque.insertFront(4); // return false (full)
    myCircularDeque.getRear();      // return 2
    myCircularDeque.isFull();       // return true
    myCircularDeque.deleteLast();   // return true
    myCircularDeque.insertFront(4); // return true
    myCircularDeque.getFront();     // return 4

Constraints:
- 1 <= k <= 1000
- 0 <= value <= 1000
- At most 2000 calls in total to the API methods


Thinking: double ended queue

"""

from typing import *

class Item:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = int(k)
        self.current_size = 0
        self.head = self.tail = None


    def _first_insert(self, value):
        item = Item(value)
        self.head = self.tail = item
        self.current_size = 1
        return True
    def insertFront(self, value: int) -> bool:
        if self.current_size >= self.max_size:
            return False
        if self.current_size == 0:
            return self._first_insert(value)
        item = Item(value, next=self.head)
        if self.head:
            self.head.prev = item
        self.head = item
        self.current_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.current_size >= self.max_size:
            return False
        if self.current_size == 0:
            return self._first_insert(value)
        item = Item(value, prev=self.tail)
        if self.tail:
            self.tail.next = item
        self.tail = item
        self.current_size += 1
        return True

    def deleteFront(self) -> bool:
        if not self.head:
            return False
        new_head = self.head.next
        if new_head:
            new_head.prev = None
        self.head = new_head
        if self.head is None:
            self.tail = None
        self.current_size -= 1
        return True

    def deleteLast(self) -> bool:
        if not self.tail:
            return False
        new_tail = self.tail.prev
        if new_tail:
            new_tail.next = None
        self.tail = new_tail
        if self.tail is None:
            self.head = None
        self.current_size -= 1
        return True

    def getFront(self) -> int:
        front = self.head
        if front:
            return front.value
        return -1

    def getRear(self) -> int:
        last = self.tail
        if last:
            return last.value
        return -1

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

if __name__ == "__main__":
    # dq = MyCircularDeque(3)
    # (dq.insertLast(1), True)
    # (dq.insertLast(2), True)
    # (dq.insertFront(3), True)
    # (dq.insertFront(4), False)
    # (dq.getRear(), 2)
    # (dq.isFull(), True)
    # (dq.deleteLast(), True)
    # (dq.insertFront(4), True)
    # (dq.getFront(), 4)

    # Additional input sequence:
    # ["MyCircularDeque","insertFront","getRear","insertFront","getRear","insertLast","getFront","getRear","getFront","insertLast","deleteLast","getFront"]
    # [[3],[9],[],[9],[],[5],[],[],[],[8],[],[]]
    dq = MyCircularDeque(3)
    results = (
        dq.insertFront(9),
        dq.getRear(),
        dq.insertFront(9),
        dq.getRear(),
        dq.insertLast(5),
        dq.getFront(),
        dq.getRear(),
        dq.getFront(),
        dq.insertLast(8),
        dq.deleteLast(),
        dq.getFront(),
    )
    print(results)


    pass
