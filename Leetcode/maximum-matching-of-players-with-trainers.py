"""
2410. Maximum Matching of Players With Trainers
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.

The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.

Return the maximum number of matchings between players and trainers that satisfy these conditions.
"""

from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players, reverse=True)
        trainers = sorted(trainers, reverse=True)
        p_length, t_length = len(players), len(trainers)
        p_idx, t_idx = 0, 0 
        while p_idx < p_length and t_idx < t_length:
            # print(p_idx, t_idx, players, trainers)
            if players[p_idx] <= trainers[t_idx]:
                p_idx += 1
                t_idx += 1
            else:
                p_idx += 1
        return t_idx
 

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players, reverse=True)
        trainers = sorted(trainers, reverse=True)
        p_idx, t_idx = 0, 0 
        while p_idx < len(players) and t_idx < len(trainers):
            # print(p_idx, t_idx, players, trainers)
            if players[p_idx] <= trainers[t_idx]:
                p_idx += 1
                t_idx += 1
            else:
                p_idx += 1
        return t_idx


players, trainers = [4,7,9], [8,2,5,8]
print(Solution().matchPlayersAndTrainers(players, trainers))


# trainer: [8, 8, 5, 2]
# player: [9, 7, 4]
