"""
Title: Design Exam Scores Tracker
URL: https://leetcode.com/problems/design-exam-scores-tracker/
Difficulty: Medium
Fetched: 2025-10-16 10:46:38

Alice frequently takes exams and wants to track her scores and compute the
total score over specified time intervals.

Implement the ExamTracker class:
- ExamTracker(): Initializes the tracker.
- record(time, score): Records a new exam taken at time with the given score.
- totalScore(startTime, endTime): Returns the total of all scores for exams
  taken between startTime and endTime inclusive. Returns 0 if none.

Function calls are made in chronological order: record() is called with
strictly increasing time, and totalScore() only queries up to the latest
recorded time.

Examples:
- Input:
  ["ExamTracker", "record", "totalScore", "record", "totalScore", "totalScore", "totalScore", "totalScore"]
  [[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]]
  Output:
  [null, null, 98, null, 98, 197, 0, 99]
  Explanation:
  examTracker = ExamTracker()
  examTracker.record(1, 98)
  examTracker.totalScore(1, 1) -> 98
  examTracker.record(5, 99)
  examTracker.totalScore(1, 3) -> 98
  examTracker.totalScore(1, 5) -> 197 (since 98 + 99)
  examTracker.totalScore(3, 4) -> 0
  examTracker.totalScore(2, 5) -> 99

Constraints:
- 1 <= time <= 10^9
- 1 <= score <= 10^9
- 1 <= startTime <= endTime <= t, where t is the latest recorded time
- Calls to record() use strictly increasing time
- After ExamTracker(), the first call is always record()
- At most 10^5 total calls to record() and totalScore()
"""

from typing import List


class ExamTracker:

    def __init__(self):
        pass

    def record(self, time: int, score: int) -> None:
        pass

    def totalScore(self, startTime: int, endTime: int) -> int:
        pass

    def check_examples(self) -> None:
        # Example sequence from the description
        self.record(1, 98)
        print(self.totalScore(1, 1))  # Expected: 98
        self.record(5, 99)
        print(self.totalScore(1, 3))  # Expected: 98
        print(self.totalScore(1, 5))  # Expected: 197
        print(self.totalScore(3, 4))  # Expected: 0
        print(self.totalScore(2, 5))  # Expected: 99


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)

if __name__ == "__main__":
    tracker = ExamTracker()
    # Run example calls (uncomment to execute):
    # tracker.check_examples()
    # Or run single custom calls:
    # tracker.record(1, 98)
    # print(tracker.totalScore(1, 1))
