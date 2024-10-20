from typing import List, Optional, Tuple
import heapq

class Graph:
    def __init__(self, n: int, directed: bool = False):
        self.n = n
        self.directed = directed
        self.L: List[List[Tuple[int, int]]] = [[] for _ in range(n)]  # List of edges (weight, vertex)


    def add_edge(self, u: int, v: int, weight: int) -> bool:
        if 0 <= u < self.n and 0 <= v < self.n:
            self.L[u].append((weight, v))
            if not self.directed:
                self.L[v].append((weight, u))  
            return True
        return False

    def DFS(self, u: int, visit: List) -> None:
        self.__DFS_visit(u, visit)

    def __DFS_visit(self, u: int, visit: List[bool]) -> None:
        visit[u] = True
        #print(u, end=' ')
        for weight, v in self.L[u]:  # Unpack the tuple correctly
            if not visit[v]:  # Check if the vertex is visited
                self.__DFS_visit(v, visit)
    

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
                self.DFS(u, visit)
                count += 1
        return count

    def is_connected(self) -> bool: #es conexo
        visit = [False] * self.n
        self.DFS(0, visit)
        return all(visit)

    def path(self, u: int, v: int) -> List[int]:
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
        parent = [-1] * self.n 

        def dfs_visit(u: int) -> bool:
            visited[u] = True
            for v in self.L[u]:
                if not visited[v]: 
                    parent[v] = u  
                    if not dfs_visit(v):
                        return False
                elif parent[u] != v:  
                    return False
            return True

        for u in range(self.n):
            if not visited[u]:  
                if not dfs_visit(u):  
                    return False
        return True

    def kruskal(self) -> List[Tuple[int, int, int]]:
        edges = []
        for u in range(self.n):
            for weight, v in self.L[u]:
                    edges.append((weight, u, v))
        
        edges.sort(key=lambda x: x[0])

        parent = list(range(self.n))
        rank = [0] * self.n

        def find(v: int) -> int:
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        def union(u: int, v: int) -> bool:
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                if rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                elif rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1
                return True
            return False

        mst_edges = []
        for weight, u, v in edges:
            if union(u, v):
                mst_edges.append((weight, u, v))

        return mst_edges

    def dijkstra(self, start: int, end: int) -> Tuple[int, List[int]]:
        distances = [float('inf')] * self.n
        distances[start] = 0

        priority_queue = [(0, start)]
        previous = [-1] * self.n 

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex == end:
                break

            
            for weight, neighbor in self.L[current_vertex]:
                distance = current_distance + weight

                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        
        path = []
        current = end
        while current != -1:
            path.append(current)
            current = previous[current]
        path.reverse()  

        return distances[end], path  

    #def show10 ():
    #    if(i=1):
    #        
    #   else:

       
g = Graph(7)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.add_edge(2, 4, 4)
g.add_edge(5,6,2)

distance, path = g.dijkstra(5, 6)
print(f"Minimum distance from vertex 0 to vertex 3: {distance}")
print(f"Path: {' -> '.join(map(str, path))}")

print ( g.is_connected())
print(g.number_of_components())