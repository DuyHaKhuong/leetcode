
from collections import defaultdict, deque 
from typing import List 

class Solution:

    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)


        visited = set([0])
        queue = [0]
        total_costs = cost[:]

        def dfs(node):
            queue = [node]
            node_cost = cost[node]
            while queue:
                u = queue.pop()
                for v in graph[u]:
                    if v in visited:
                        continue 
                    visited.add(v)
                    queue.append(v)

                    v_cost = dfs(v)
                    node_cost = max(node_cost, v_cost + cost[node])

            print(node, node_cost)
            return node_cost
        return dfs(0)

        queue = [0]
        while queue:
            u = queue.pop()

            max_cost, count = float('-inf'), 0
            print(u)
            nodes = [v for v in graph[u] if v not in visited]
            for v in nodes:
                queue.append(v)
                visited.add(v)

        pass 

    def minIncreaseV1(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        depths = [-1] * n 
        depths[0] = 0
        depth_map = defaultdict(list)
        depth_map[0].append(0)
        queue = deque([0])

        tree = defaultdict(set)
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if depths[v] != -1:  # already visited
                    continue 
                tree[u].add(v)
                depths[v] = depths[u] + 1 
                queue.append(v)
                depth_map[depths[v]].append(v)
        
        max_depth = max(depths)
        total_costs = cost[:]
        n_updates = 0
        print(graph)
        for depth in range(max_depth - 1, -1, -1):
            print(depth, depth_map[depth])
            for u in depth_map[depth]:
                nodes = tree[u]
                if len(nodes) == 0:
                    continue
                max_cost = max(total_costs[n] for n in nodes)
                n_updates += sum(max_cost != total_costs[n] for n in nodes)
                # print("update", u,nodes,  n_updates)
                total_costs[u] += max_cost
        return n_updates 


# n = 3, edges = [[0,1],[0,2]], cost = [2,1,3]
print(Solution().minIncrease(3, [[0,1],[0,2]], [2,1,3]))
# n = 3, edges = [[0,1],[1,2]], cost = [5,1,4]
# print(Solution().minIncrease(3, [[0,1],[1,2]], [5,1,4]))