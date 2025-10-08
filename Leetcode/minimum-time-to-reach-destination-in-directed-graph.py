"""
3604. Minimum Time to Reach Destination in Directed Graph
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer n and a directed graph with n nodes labeled from 0 to n - 1. This is represented by a 2D array edges, where edges[i] = [ui, vi, starti, endi] indicates an edge from node ui to vi that can only be used at any integer time t such that starti <= t <= endi.

You start at node 0 at time 0.

In one unit of time, you can either:

Wait at your current node without moving, or
Travel along an outgoing edge from your current node if the current time t satisfies starti <= t <= endi.
Return the minimum time required to reach node n - 1. If it is impossible, return -1.
""" 

from typing import List 
from collections import defaultdict 

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        START = 0 
        END = 1 
        sorted_edges = []
        for u, v, start, end in edges:
            sorted_edges.append((start, u, v, START))
            sorted_edges.append((end, u, v, END))
        sorted_edges.sort()

        earliest_times = [float('inf')] * n 
        earliest_times[0] = 0
        current_nodes = set([0]) 
        time = -1
        graph = defaultdict(set)
        idx = 0 
        while True:
            time += 1
            # Update graph
            while idx < len(sorted_edges) and sorted_edges[idx][0] <= time:
                t, u, v, start_or_end = sorted_edges[idx]
                if start_or_end == START:
                    graph[u].add(v)
                else:
                    graph[u].remove(v)
                idx += 1
            



