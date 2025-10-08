"""
LeetCode: Meeting Scheduler
URL: https://leetcode.com/problems/meeting-scheduler/
Difficulty: Medium
Fetched: 2025-10-06 10:13:21

Description:
You are given two lists of available time slots, slots1 and slots2, and an integer
duration. Each slot is an interval [start, end], where start < end, representing a
time window when a person is available. Return the earliest time interval of length
duration that appears in both lists (i.e., an interval [x, x + duration] such that
for some [s1, e1] in slots1 and [s2, e2] in slots2, max(s1, s2) <= x and x + duration <= min(e1, e2)).
If there is no such common slot, return an empty list [].

Examples:
- Example 1
  Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
  Output: [60, 68]
  Explanation: The earliest common slot of at least 8 minutes is [60, 68].

- Example 2
  Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
  Output: []
  Explanation: No common slot of length 12 exists.

Constraints:
- 1 <= slots1.length, slots2.length <= 10^4
- slots[i].length == 2
- 0 <= start < end <= 10^9
- 1 <= duration <= 10^6
"""

from typing import *


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        all_slots = ([
            *[(s, True, 0) for s, e in slots1],
            *[(e, False, 0) for s, e in slots1],
            *[(s, True, 1) for s, e in slots2],
            *[(e, False, 1) for s, e in slots2],
        ])
        all_slots.sort(key=lambda x: x[0])

        start_times = {}
        for t, is_start, person in all_slots:
            if is_start:
                start_times[person] = t
            else:
                other = 1 - person
                if other not in start_times:
                    continue
                durations = [
                    t - start_times[person],
                    t - start_times[other],
                ]
                if min(durations) >= duration:
                    s = max(start_times[person], start_times[other])
                    return [s, s + duration]
                del start_times[person]
        return []


if __name__ == "__main__":
    # Code to run examples (not tests)
    sol = Solution()
    print(sol.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8))   # Expected: [60, 68]
    print(sol.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12))  # Expected: []
