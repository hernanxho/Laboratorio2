from typing import List, Optional, Tuple, Any, Set, Dict
import heapq
import haversine as h
import pandas as pd

df = pd.read_csv("./data/flights_final.csv")


class Graph:

    def __init__(self, n: int, directed: bool = False):
        self.n = n
        self.directed = directed
        self.L: List[List[Tuple[int, float]]] = [[] for _ in range(n)]   #(vertix, weight)
        self.dataGraph: Dict[int, Dict] = {}  
    
    def infoAirport(self, idx: int, info: Dict):
        self.dataGraph[idx] = info

    def add_edge(self, u: int, v: int, lat_u: float, lon_u: float, lat_v: float, lon_v: float) -> bool:
        if 0 <= u < self.n and 0 <= v < self.n:
            weight = h.haversine((lat_u, lon_u), (lat_v, lon_v))
            self.L[u].append((v, weight))
            if not self.directed:
                self.L[v].append((u, weight))
            return True
        return False
    

    def kruskal(self): #kruskal que retorna peso del subgrafo generado y las aristas usadas
        edges = []
        for u in range(self.n):
            for v, weight in self.L[u]:
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

    def is_connected(self) -> Tuple[bool, List[List[int]]]: # Retorna un booleano sobre si es conexo y una lista tuplas de los vertices de cada componente
        visited = [False] * self.n
        components = []

        def dfs(u, component):
            visited[u] = True
            component.append(u)
            for v, _ in self.L[u]:
                if not visited[v]:
                    dfs(v, component)

        for u in range(self.n):
            if not visited[u]:
                component = []
                dfs(u, component)
                components.append(component)

        is_connected = len(components) == 1
        return is_connected, components



    
    def Dijkstra(self, start: int) -> Dict[int, Tuple[float, List[int]]]:  # Dijkstra desde un v1 y retorna un diccionario donde la key es el vertice con el que busco caminno minimo
                                                                         # y el valor es una tupla con el peso del camino minimo y la lista de los vertices que generan el camino      

        dist = {i: float('inf') for i in range(self.n)}
        dist[start] = 0
        prev = {i: None for i in range(self.n)}
        visited = [False] * self.n

        for _ in range(self.n):
            min_dist = float('inf')
            u = -1
            for i in range(self.n):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i
            
            if u == -1:  
                break
            
            visited[u] = True

            for v, weight in self.L[u]:
                if not visited[v]: 
                    new_dist = dist[u] + weight
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        prev[v] = u

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
    
    def mst_weight_per_component(self) -> Dict[int, float]: #peso de cada componente
        is_connected, components = self.is_connected()

        if is_connected:
            mst_weight, _ = self.kruskal()
            return {0: mst_weight} 

        else:
            component_weights = {}
            for idx, component in enumerate(components):
                subgraph = Graph(len(component))
                node_mapping = {node: i for i, node in enumerate(component)}

                for u in component:
                    for v, weight in self.L[u]:
                        if v in component:
                            added = subgraph.add_edge(node_mapping[u], node_mapping[v], 
                                                        self.dataGraph[u]['latitude'], 
                                                        self.dataGraph[u]['longitude'], 
                                                        self.dataGraph[v]['latitude'], 
                                                        self.dataGraph[v]['longitude'])
                mst_weight, _ = subgraph.kruskal() #peso de cada subgrafo
                component_weights[idx+1] = mst_weight
                #print(f"Peso del MST para la componente {idx}: {mst_weight:.2f}")  esto fue nada mas para el debugging

            return component_weights
    
    def obtener_info(self, code: str):
        code = code.strip().upper()
        
        if code in indexAirport:
            idx = indexAirport[code]
            if idx in self.dataGraph:
                return self.dataGraph[idx]
            else:
                return "No information available for this airport."
        else:
            return "Airport code does not exist."


indexAirport = dict()
current_idx = 0

for index, row in df.iterrows():
    source_code = row['Source Airport Code']
    dest_code = row['Destination Airport Code']

    # Asignar índices a los aeropuertos si aún no lo tienen
    if source_code not in indexAirport:
        indexAirport[source_code] = current_idx
        current_idx += 1
    if dest_code not in indexAirport:
        indexAirport[dest_code] = current_idx
        current_idx += 1

# Crear el grafo con el número total de aeropuertos(aun no se muestra,ok?)
n_airports = len(indexAirport)
g = Graph(n_airports)

# Agregar las aristas y la información de los aeropuertos al grafo
for index, row in df.iterrows():
    u = indexAirport[row['Source Airport Code']]
    v = indexAirport[row['Destination Airport Code']]
    lat_u, lon_u = row['Source Airport Latitude'], row['Source Airport Longitude']
    lat_v, lon_v = row['Destination Airport Latitude'], row['Destination Airport Longitude']
    
    g.add_edge(u, v, lat_u, lon_u, lat_v, lon_v)

    # Agregar información del aeropuerto
    g.infoAirport(u, {
        'code': row['Source Airport Code'],
        'name': row['Source Airport Name'],
        'city': row['Source Airport City'],
        'country': row['Source Airport Country'],
        'latitude': lat_u,
        'longitude': lon_u
    })
    g.infoAirport(v, {
        'code': row['Destination Airport Code'],
        'name': row['Destination Airport Name'],
        'city': row['Destination Airport City'],
        'country': row['Destination Airport Country'],
        'latitude': lat_v,
        'longitude': lon_v
    })


           
#g.add_edge()

#distance, path = g.dijkstra(5, 6)
#print(f"Minimum distance from vertex 0 to vertex 3: {distance}")
#print(f"Path: {' -> '.join(map(str, path))}")


conection, n_components = g.is_connected()
#print(f"Number of connected components: {len(n_components)}")
#print(g.L[1])
#print (g.weights_components(n_components))
#print(g.mst_weight_per_component())
# Example of calculating the MST
#mst_weight, mst_edges = g.kruskal()
#print(f"MST Weight: {mst_weight}")
#print("MST Edges:", mst_edges)
#print(n_components)
#print(g.airport_data[3103])
#print(g.Dijkstra(3103))
#print(g.airport_data[2565], g.airport_data[2566])
#mst_weight, mst_edges = g.kruskal()
#print(mst_edges)

