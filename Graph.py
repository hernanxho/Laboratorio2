from typing import List, Optional

class Graph:
    def __init__(self, n: int, directed: bool = False):
        self.n = n
        self.directed = directed
        self.L: List[List[int]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int) -> bool:
        if 0 <= u < self.n and 0 <= v < self.n:
            self.L[u].append(v)
            self.L[u].sort()
            if not self.directed:
                self.L[v].append(u)
                self.L[v].sort()
            return True
        return False

    def DFS(self, u: int) -> None:
        visit = [False] * self.n
        self.__DFS_visit(u, visit)

    def __DFS_visit(self, u: int, visit: List[bool]) -> List[bool]:
        visit[u] = True
        print(u, end=' ')
        for v in self.L[u]:
            if not visit[v]:
                self.__DFS_visit(v, visit)
        return visit
    

    def BFS(self, u: int) -> None:
        queue = []
        visit = [False] * self.n
        visit[u] = True
        queue.append(u)
        while len(queue) > 0:
            u = queue.pop(0)
            print(u, end=' ')
            for v in self.L[u]:
                if not visit[v]:
                    visit[v] = True
                    queue.append(v)

    def degree(self, u: int) -> int:
        if 0 <= u < self.n:
            return len(self.L[u])
        return -1

    def min_degree(self) -> int:
        #Returns the minimum degree of the graph
        return min(self.degree(u) for u in range(self.n))

    def max_degree(self) -> int:
        #Returns the maximum degree of the graph
        return max(self.degree(u) for u in range(self.n))

    def degree_sequence(self) -> List[int]:
        return sorted((self.degree(u) for u in range(self.n)), reverse=True)

    def number_of_components(self) -> int:
        visit = [False] * self.n
        count = 0
        for u in range(self.n):
            if not visit[u]:
                self.DFS(u)
                count += 1
        return count

    def is_connected(self) -> bool: #es conexo
        visit = [False] * self.n
        self.DFS(0)
        return all(visit)

    def path(self, u: int, v: int) -> List[int]:
        """Finds a path from u to v using DFS."""
        visited = [False] * self.n
        path = []
        if self.__find_path(u, v, visited, path):
            return path
        return []

    def __find_path(self, u: int, v: int, visited: List[bool], path: List[int]) -> bool:
        visited[u] = True
        path.append(u)
        if u == v:
            return True
        for neighbor in self.L[u]:
            if not visited[neighbor]:
                if self.__find_path(neighbor, v, visited, path):
                    return True
        path.pop()
        return False

    def is_eulerian(self) -> bool:
        if self.is_connected():
            return all(self.degree(u) % 2 == 0 for u in range(self.n))
        return False

    def is_semieulerian(self) -> bool:
        if self.is_connected():
            odd_degree_count = sum(1 for u in range(self.n) if self.degree(u) % 2 != 0)
            return odd_degree_count == 2
        return False

    def is_r_regular(self, r: int) -> bool:
        return all(self.degree(u) == r for u in range(self.n))

    def is_complete(self) -> bool:
        for u in range(self.n):
            if self.degree(u) != self.n - 1:
                return False
        return True

    def is_acyclic(self) -> bool:
        visited = [False] * self.n
        parent = [-1] * self.n  # To keep track of the parent nodes

        def dfs_visit(u: int) -> bool:
            visited[u] = True
            for v in self.L[u]:
                if not visited[v]:  # If the node is not visited
                    parent[v] = u  # Set parent
                    if not dfs_visit(v):  # Continue DFS
                        return False
                elif parent[u] != v:  # If visited and not the parent, there's a cycle
                    return False
            return True

        for u in range(self.n):
            if not visited[u]:  # If the node is not visited, start DFS
                if not dfs_visit(u):  # If a cycle is detected
                    return False
        return True