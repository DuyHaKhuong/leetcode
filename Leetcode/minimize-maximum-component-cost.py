"""
3613. Minimize Maximum Component Cost
Medium
premium lock icon
Companies
Hint
You are given an undirected connected graph with n nodes labeled from 0 to n - 1 and a 2D integer array edges where edges[i] = [ui, vi, wi] denotes an undirected edge between node ui and node vi with weight wi, and an integer k.

You are allowed to remove any number of edges from the graph such that the resulting graph has at most k connected components.

The cost of a component is defined as the maximum edge weight in that component. If a component has no edges, its cost is 0.

Return the minimum possible value of the maximum cost among all components after such removals.
"""

from typing import List 

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        edges = sorted(edges, key=lambda e: e[2])
        parents = list(range(n))

        def find(node):
            p = parents[node]
            if p == node:
                return p 
            grandparent = find(p)
            parents[node] = grandparent 
            return grandparent 
        
        n_components = n
        max_weight = 0
        for u, v, w in edges:
            if n_components <= k:
                return max_weight
            # Add new edge
            pu, pv = find(u), find(v)
            if pu == pv:
                continue 
            # Two components need to be merged into one 
            parents[pu] = parents[pv] = min(pu, pv)
            n_components -= 1 
            max_weight = max(max_weight, w)
        
        return max_weight