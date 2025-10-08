"""
3608. Minimum Time for K Connected Components
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer n and an undirected graph with n nodes labeled from 0 to n - 1. This is represented by a 2D array edges, where edges[i] = [ui, vi, timei] indicates an undirected edge between nodes ui and vi that can be removed at timei.

You are also given an integer k.

Initially, the graph may be connected or disconnected. Your task is to find the minimum time t such that after removing all edges with time <= t, the graph contains at least k connected components.

Return the minimum time t.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
"""


from typing import List 
from collections import defaultdict, deque

class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:

        parents = list(range(n))
        def find(u):
            v = parents[u]
            if u == v:
                return u 
            parents[u] = find(v)
            return parents[u]

        def union(u, v):
            a = find(u)
            b = find(v)
            if a == b:
                return False 
            parents[a] = b 
            return True

        edges = sorted(edges, key = lambda e: -e[2])
        cnt = n 
        for u, v, t in edges:
            is_separated = union(u, v)
            if is_separated:
                cnt -= 1 
            if cnt == k - 1:
                return t 
        pass 

    def minTimeV1(self, n: int, edges: List[List[int]], k: int) -> int:
        edges = sorted(edges, key = lambda e: e[2])
        graph = defaultdict(set)
        for u, v, t in edges:
            graph[u].add(v)
            graph[v].add(u)

        def bfs(node):
            components = set([node])
            queue = deque([node])
            while queue:
                u = queue.popleft()
                neighbors = graph[u]
                for v in neighbors:
                    if v in components:
                        continue 
                    components.add(v)
                    queue.append(v)
            return min(components), components

        def is_connected(u, v):
            visited = set()
            queue = deque([u])
            while queue:
                u = queue.popleft()
                visited.add(u)
                neighbors = graph[u]
                for v in neighbors:
                    if v in visited:
                        continue 
                    if u == v:
                        return True 
                    queue.append(v)
            return False 
        
        # Find connected components 
        component_map = [-1] * n 
        n_connected_components = 0
        for node in range(n):
            if component_map[node] != -1:
                continue 
            # Find connected component for this node 
            min_node, nodes = bfs(node)
            for u in nodes:
                component_map[u] = min_node
            n_connected_components += 1

        if n_connected_components >= k:
            return 0

        # Update the graph each time 
        for u, v, t in edges:
            graph[u].remove(v)
            graph[v].remove(u)
            if is_connected(u, v):
                continue 
            min_u, u_components = bfs(u)
            min_v, v_components = bfs(v)
            if min_v == min_u == component_map[u]:
                continue
            n_connected_components += 1
            if n_connected_components >= k:
                return t

            for u in u_components:
                component_map[u] = min_u
            for v in v_components:
                component_map[v] = min_v
        
        return -1


n, edges, k = 2, [[0,1,3]], 2
n, edges, k = 3, [[0,1,2],[1,2,4]], 3
# n, edges, k = 3, [[0,2,5]], 2
print(Solution().minTime(n, edges, k))
