from typing import List, Optional, Tuple, Any, Set, Dict
import heapq
import haversine as h
import pandas as pd




class Graph:

    def __init__(self, n: int, directed: bool = False):
        self.n = n
        self.directed = directed
        self.L: List[List[Tuple[int, float]]] = [[] for _ in range(n)]  
        self.airport_data: Dict[int, Dict] = {}  
    
    def add_airport_info(self, idx: int, info: Dict):
        self.airport_data[idx] = info

    def add_edge(self, u: int, v: int, lat_u: float, lon_u: float, lat_v: float, lon_v: float) -> bool:
        if 0 <= u < self.n and 0 <= v < self.n:
            weight = h.haversine((lat_u, lon_u), (lat_v, lon_v))
            self.L[u].append((v, weight))
            if not self.directed:
                self.L[v].append((u, weight))
            return True
        return False
    

    def kruskal(self):
        edges = []
        for u in range(self.n):
            for v, weight in self.L[u]:
                if u < v:  
                    edges.append((weight, u, v))

        edges.sort()

        parent = list(range(self.n)) 
        rank = [0] * self.n

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
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


        mst_weight = 0
        mst_edges = []
        for weight, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                mst_weight += weight
                mst_edges.append((u, v, weight))

        return mst_weight, mst_edges

    def is_connected(self) -> Tuple[bool, List[Set[int]]]:
        visited = [False] * self.n
        components = []

        def dfs(u, component):
            visited[u] = True
            component.add(u)
            for v, _ in self.L[u]:
                if not visited[v]:                                 
                    dfs(v, component)
                    
    
        for u in range(self.n):
            if not visited[u]:
                component = set()
                dfs(u, component, )
                components.append(component)

        is_connected = len(components) == 1
        return is_connected, components
    
    def weights_components (self, components):
        weights = []
        for  component in components:
            weight = 0
            for  u in component:
                for i in self.L[u]:
                    weight = weight + i[1]
                    print(i[1])

            weights.append(weight)
        return weights


    
    def Dijkstra(self, start: int) -> Dict[int, Tuple[float, List[int]]]:
        import heapq
        dist = {i: float('inf') for i in range(self.n)}
        dist[start] = 0
        prev = {i: None for i in range(self.n)}
        pq = [(0, start)]  

        while pq:
            current_dist, u = heapq.heappop(pq)
            if current_dist > dist[u]:
                continue

            for v, weight in self.L[u]:
                new_dist = current_dist + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = u
                    heapq.heappush(pq, (new_dist, v))

        paths = {}
        for v in range(self.n):
            if dist[v] < float('inf'):
                path = []
                node = v
                while node is not None:
                    path.append(node)
                    node = prev[node]
                paths[v] = (dist[v], path[::-1])

        return paths

df = pd.read_csv("./data/flights_final.csv")

airport_to_idx = {}
current_idx = 0

for index, row in df.iterrows():
    source_code = row['Source Airport Code']
    dest_code = row['Destination Airport Code']

    if source_code not in airport_to_idx:
        airport_to_idx[source_code] = current_idx
        current_idx += 1
    if dest_code not in airport_to_idx:
        airport_to_idx[dest_code] = current_idx
        current_idx += 1

g = Graph(len(airport_to_idx))

# Agregar las aristas y la información de los aeropuertos al grafo
for index, row in df.iterrows():
    u = airport_to_idx[row['Source Airport Code']]
    v = airport_to_idx[row['Destination Airport Code']]
    lat_u, lon_u = row['Source Airport Latitude'], row['Source Airport Longitude']
    lat_v, lon_v = row['Destination Airport Latitude'], row['Destination Airport Longitude']
    
    g.add_edge(u, v, lat_u, lon_u, lat_v, lon_v)

    # Agregar información del aeropuerto
    g.add_airport_info(u, {
        'code': row['Source Airport Code'],
        'name': row['Source Airport Name'],
        'city': row['Source Airport City'],
        'country': row['Source Airport Country'],
        'latitude': lat_u,
        'longitude': lon_u
    })
    g.add_airport_info(v, {
        'code': row['Destination Airport Code'],
        'name': row['Destination Airport Name'],
        'city': row['Destination Airport City'],
        'country': row['Destination Airport Country'],
        'latitude': lat_v,
        'longitude': lon_v
    })
       
g.n = len(g.L)
#g.add_edge()

#distance, path = g.dijkstra(5, 6)
#print(f"Minimum distance from vertex 0 to vertex 3: {distance}")
#print(f"Path: {' -> '.join(map(str, path))}")


conection, n_components = g.is_connected()
print(f"Number of connected components: {len(n_components)}")
#print(g.L[1])
print (g.weights_components(n_components))
#print(n_components)
#print(g.airport_data[2565], g.airport_data[2566])
#mst_weight, mst_edges = g.kruskal()
#print(mst_edges)

