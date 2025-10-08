"""
You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).

These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.

Initially, all stations are online (operational).

You are also given a 2D array queries, where each query is one of the following two types:

[1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. If no operational station exists in that grid, return -1.

[2, x]: Station x goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type [1, x] in the order they appear.

Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.
"""

from typing import List 
from collections import defaultdict, deque

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parents = list(range(c + 1))
        def find(node):
            p = parents[node]
            if p == node:
                return p 
            gp = find(p)
            parents[node] = gp 
            return gp 

        for u, v in connections:
            a, b = find(u), find(v)
            parents[a] = parents[b] = min(a, b)

        grid_map = [None] * (c + 1)
        components = defaultdict(list)
        for node in range(c, 0, -1):
            p = find(node)
            components[p].append(node)
            grid_map[node] = components[p]
        
        status = [True] * (c + 1)
        results = []
        for action, node in queries:
            if action == 2:
                status[node] = False 
                components = grid_map[node]
                while components and status[components[-1]] == False:
                    components.pop()
            # action == 1: maintenance check 
            elif status[node]:
                results.append(node)
            else:
                if not grid_map[node]:
                    results.append(-1)
                else:
                    results.append(grid_map[node][-1])
        return results


    def processQueriesV1(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in connections:
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
            return sorted(components, reverse=True)

        grid_map = [None] * (c + 1)
        for node in range(1, c + 1):
            if grid_map[node] is not None:
                continue 
            components = bfs(node)
            for u in components:
                grid_map[u] = components

        
        status = [True] * (c + 2)
        results = []
        for action, node in queries:
            if action == 2:
                status[node] = False 
                components = grid_map[node]
                while components and status[components[-1]] == False:
                    components.pop()
            # action == 1: maintenance check 
            elif status[node]:
                results.append(node)
            else:
                if not grid_map[node]:
                    results.append(-1)
                else:
                    results.append(grid_map[node][-1])
        return results


# c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
c, connections, queries = 5, [[1,2],[2,3],[3,4],[4,5]], [[1,3],[2,1],[1,1],[2,2],[1,2]]
print(Solution().processQueries(c, connections, queries))
