"""
Title: Earliest Finish Time for Land and Water Rides II
URL: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/
Difficulty: Medium
Fetched: 2025-09-29 21:03:59

Description:
There are two categories of theme park rides: land and water. For land rides,
`landStartTime[i]` and `landDuration[i]` give the earliest time ride i opens
and how long it lasts. Similarly, for water rides you are given
`waterStartTime[j]` and `waterDuration[j]`.

You must take exactly one land ride and one water ride in either order. You may
start a ride at its opening time or any later time. If a ride starts at time t,
it finishes at t + duration. After finishing one ride, you may board the other
immediately if it is open; otherwise, wait until it opens.

Return the earliest possible time at which both rides can be finished.

Examples:
- Input: landStartTime = [2, 8], landDuration = [4, 1], waterStartTime = [6], waterDuration = [3]
  Output: 9
  Explanation: Do land(0) from 2→6, then water(0) 6→9.

- Input: landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]
  Output: 14
  Explanation: Do water(0) 1→11, then land(0) 11→14.

Constraints:
- 1 <= n, m <= 5e4
- landStartTime.length == landDuration.length == n
- waterStartTime.length == waterDuration.length == m
- 1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 1e5

Thinking:
land -> water -> land -> water ...

"""

from typing import *
from dataclasses import dataclass
from functools import cached_property


from typing import *


class Solution:
    def earliestFinishTime(
            self,
            landStartTime: List[int],
            landDuration: List[int],
            waterStartTime: List[int],
            waterDuration: List[int],
    ) -> int:
        """Pick one land + one water in either order; return earliest finish time.

        Placeholder stub per repository guidelines; implement on LeetCode.
        """
        N, M = len(landStartTime), len(waterStartTime)
        landTime = [(s, s + d) for s, d in zip(landStartTime, landDuration)]
        waterTime = [(s, s + d) for s, d in zip(waterStartTime, waterDuration)]
        # Land -> water

        def find_min_finish(first_activities, second_activities, max_time=None):
            # first_activities sorted by finish time
            first_activities.sort(key=lambda x: x[1])
            # second_activities sorted by start time
            second_activities.sort(key=lambda x: x[0])
            # print(first_activities)
            # print(second_activities)
            # Create min_finishes for 2nd activity starting at the finishTime[j]
            N, M = len(first_activities), len(second_activities)

            # min duration before 2nd activity j
            # Use this min duration if the 1st activity starts after 2nd activity j start time
            min_duration = float('inf')
            min_durations = [min_duration]
            for s, e in second_activities:
                min_duration = min(
                    min_duration,
                    e - s,
                )
                min_durations.append(min_duration)

            min_finishes = [0] * M
            min_finish = float('inf')
            for j in range(M - 1, -1, -1):
                min_finish = min(
                    min_finish,
                    second_activities[j][0] + min_durations[j],
                    second_activities[j][1],
                )
                min_finishes[j] = min_finish

            k = 0
            ans = max_time or float('inf')
            for istart, ifinish in first_activities:
                if ifinish >= ans:
                    return ans
                while k < M and second_activities[k][0] < ifinish:
                    k += 1
                if k == M:
                    ans = min(ans, ifinish + min_durations[-1])
                    break
                ans = min(
                    ans,
                    min_finishes[k],
                    ifinish + min_durations[k],
                )

            return ans

        c1 = find_min_finish(landTime, waterTime)
        c2 = find_min_finish(waterTime, landTime, c1)
        # print(c1, c2)
        return min(c1, c2)

@dataclass
class Activity:
    start_time: int
    duration: int

    @cached_property
    def end_time(self):
        return self.start_time + self.duration


class Solution2:
    def earliestFinishTimeV2(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        """Pick one land + one water in either order; return earliest finish time.

        Placeholder stub per repository guidelines; implement on LeetCode.
        """
        land_activities = [
            Activity(s, d) for s, d in zip(landStartTime, landDuration)
        ]
        water_activities = [
            Activity(s, d) for s, d in zip(waterStartTime, waterDuration)
        ]

        def find_min_finish(first_activities, second_activities):
            # first_activities sorted by finish time
            first_activities.sort(key=lambda x: x.end_time)
            # second_activities sorted by start time
            second_activities.sort(key=lambda x: x.start_time)
            # Create min_finishes for 2nd activity starting at the finishTime[j]
            N, M = len(first_activities), len(second_activities)

            # min duration before 2nd activity j
            # Use this min duration if the 1st activity starts after 2nd activity j start time
            min_duration = float('inf')
            min_durations = [min_duration]
            for a in second_activities:
                min_duration = min(
                    min_duration,
                    a.duration,
                )
                min_durations.append(min_duration)

            min_finishes = [0] * M
            min_finish = float('inf')
            for j in range(M - 1, -1, -1):
                min_finish = min(
                    min_finish,
                    second_activities[j].start_time + min_durations[j],
                    second_activities[j].end_time,
                )
                min_finishes[j] = min_finish
            # print(min_durations)
            # print(min_finishes)

            k = 0
            ans = float('inf')
            for a in first_activities:
                if a.end_time > ans:
                    return ans
                while k < M and second_activities[k].start_time < a.end_time:
                    k += 1
                if k == M:
                    ans = min(ans, a.end_time + min_durations[-1])
                    break
                ans = min(
                    ans,
                    min_finishes[k],
                    # second_activities[k][1],
                    a.end_time + min_durations[k],
                )

            return ans

        # Land -> water
        c1 = find_min_finish(land_activities, water_activities)
        # water -> land
        c2 = find_min_finish(water_activities, land_activities)
        # print(c1, c2)
        return min(c1, c2)

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    # self.assertEqual(
    #     sol.earliestFinishTime([2, 8], [4, 1], [6], [3]), 9
    # )
    # Example 2
    # print(
    #     sol.earliestFinishTime([5], [3], [1], [10]), 14
    # )
    # print(
    #     sol.earliestFinishTime([2, 8], [4, 1], [6], [3]), 9
    # )
    #
    # print(sol.earliestFinishTime(
    #     [41,59,14],
    #     [8,74,45],
    #     [41,78],
    #     [16,33]
    # ))

    print(
        sol.earliestFinishTime(
            [8,48],
            [28,63],
            [61,87,24,75,64],
            [31,58,71,67,13],
        )
    )

    # Uncomment to run tests locally
    # unittest.main(verbosity=2)

