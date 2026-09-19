class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = {i: [] for i in range(n)}
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        def dfs(node, pair):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == pair: continue
                if not dfs(neighbor, node): return False
            
            return True
                
        return dfs(0, -1) and len(visited) == n

         
        