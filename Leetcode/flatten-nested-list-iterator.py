"""
LeetCode: Flatten Nested List Iterator
URL: https://leetcode.com/problems/flatten-nested-list-iterator/
Difficulty: Medium
Fetched: 2025-10-06 15:36:53

Description:
You are given a nested list of integers nestedList. Each element is either an integer
or a list whose elements may themselves be integers or other lists. Implement an
iterator to flatten it.

Implement the class NestedIterator with:
- NestedIterator(nestedList): Initialize the iterator with the nested list.
- next(): Return the next integer in the nested list.
- hasNext(): Return true if there are still integers remaining, false otherwise.

Testing pseudocode:
  initialize iterator with nestedList
  res = []
  while iterator.hasNext():
      res.append(iterator.next())
  return res

If res matches the expected flattened list, the solution is correct.

Examples:
- Example 1
  Input: nestedList = [[1, 1], 2, [1, 1]]
  Output: [1, 1, 2, 1, 1]
  Explanation: next returns values in order until hasNext is false.

- Example 2
  Input: nestedList = [1, [4, [6]]]
  Output: [1, 4, 6]

Constraints:
- 1 <= nestedList.length <= 500
- -10^6 <= integer value <= 10^6
"""

from typing import *
class NestedInteger:
    def __init__(self, value=None):
        if isinstance(value, list):
            self._integer = None
            self._list = [NestedInteger(v) for v in value]
        else:
            self._integer = value
            self._list = None

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> Optional[int]:
        return self._integer

    def getList(self) -> List['NestedInteger']:
        return self._list or []


class NestedIterator:
    def __init__(self, nestedList):
        self.nested_list = nestedList
        self.current_index = 0
        self.has_next_in_loop = len(nestedList) > 0
        self.has_next = len(nestedList) > 0

    def _yield(self, nested_integer):
        if nested_integer.isInteger():
            self.has_next_in_loop = False
            k = nested_integer.getInteger()
            print(k)
            yield k
        else:
            integer_list = nested_integer.getList()
            for i, ni in enumerate(integer_list):
                self.has_next_in_loop = i < len(integer_list) - 1
                yield from self._yield(ni)

    def next(self) -> int:
        for i, nested_integer in enumerate(self.nested_list):
            self.has_next = i < len(self.nested_list) - 1
            yield from self._yield(nested_integer)

    def hasNext(self) -> bool:
        # return self.has_next_in_loop or self.has_next
        return self.has_next

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

if __name__ == "__main__":
    # Code to run examples (not tests)
    # Minimal local NestedInteger implementation for running examples
    # Rebind the type name for this local run
    NestedIntegerType = NestedInteger

    # Example runner that uses NestedIterator
    def run_example(data):
        # Convert Python nested structure to NestedInteger list
        nested = [NestedInteger(d) for d in data]
        it = NestedIterator(nested)  # type: ignore[name-defined]
        out = []
        while getattr(it, 'hasNext')():
            out.append(getattr(it, 'next')())
        return out

    # Examples
    print(run_example([[1, 1], 2, [1, 1]]))  # Expected: [1, 1, 2, 1, 1]
    print(run_example([1, [4, [6]]]))        # Expected: [1, 4, 6]
