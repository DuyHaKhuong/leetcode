"""
3440. Reschedule Meetings for Maximum Free Time II
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.

These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, to maximize the longest continuous period of free time during the event.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.

Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.
""" 

from typing import List 

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0] * n 
        start_free_time = 0
        max_free_time = 0
        for i in range(n):
            gaps[i] = startTime[i] - start_free_time
            start_free_time = endTime[i]
            max_free_time = max(max_free_time, gaps[i])

        max_gap_before = [0] * n 
        max_gap_after = [0] * n 
        max_gap_before[0] = gaps[0]
        for i in range(1, n):
            max_gap_before[i] = max(max_gap_before[i - 1], gaps[i])
        max_gap_after[n - 1] = eventTime - endTime[n - 1]
        for i in range(n - 2, -1, -1):
            max_gap_after[i] = max(max_gap_after[i + 1], gaps[i + 1])

        print(gaps)
        print(max_gap_before)
        print(max_gap_after)

        for i in range(n):
            # Consider move meeting i to have more free time
            # Check the maximum gap after moving from start_free_time to endTime[i + 1]
            start_free_time = endTime[i - 1] if i > 0 else 0
            end_free_time = startTime[i + 1] if (i < n - 1) else eventTime
            free_time = end_free_time - start_free_time
            if free_time <= max_free_time:
                continue 
            duration = endTime[i] - startTime[i]
            # Move to side: endTime[i] -> startTime[i + 1]
            side_free_time = free_time - duration
            if side_free_time > max_free_time:
                max_free_time = side_free_time

            # Move outside if possible
            if i > 0 and duration <= max_gap_before[i - 1]:
                max_free_time = max(max_free_time, free_time)
            if i < n - 1 and duration <= max_gap_after[i + 1]:
                max_free_time = max(max_free_time, free_time)
        return max_free_time


eventTime, startTime, endTime = 5, [1,3], [2,5]
eventTime, startTime, endTime = 10, [0,7,9], [1,8,10]
eventTime, startTime, endTime = 10, [0,3,7,9], [1,4,8,10]
eventTime, startTime, endTime = 5, [0,1,2,3,4], [1,2,3,4,5]
print(Solution().maxFreeTime(eventTime, startTime, endTime))
