class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, origen, destino):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append(destino)
            self.vertices[destino].append(origen)

    def obtener_vertices(self):
        return list(self.vertices.keys())
    
    def obtener_aristas(self):
        aristas = []
        for vertice, adyacentes in self.vertices.items():
            for adyacente in adyacentes:
                aristas.append((vertice, adyacente))
        return aristas
    

grafo = Grafo()

grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")

grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")
grafo.agregar_arista("B", "C")

vertices = grafo.obtener_vertices()
print("Vértices:", vertices)
aristas = grafo.obtener_aristas()
print("Aristas:", aristas)