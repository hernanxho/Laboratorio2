from typing import List, Optional
from AereopuertoClass import*
import pandas as pd

df = pd.read_csv("./data/flights_final.csv")

class Mapa:
    def __init__(self,aeropuertos: Optional[List['Aeropuerto']] = None):
        self.aeropuertos = aeropuertos if aeropuertos is not None else []
    
    def agregar(self):
        for index, row in df.iterrows():
            nuevo_aeropuerto = Aeropuerto(row['Source Airport Name'],row['Source Airport Latitude'],row['Source Airport Longitude'])
            self.aeropuertos.append(nuevo_aeropuerto)
    
    #def agregar_data(self):
        #for index, row in df.iterrows():
            #self.agregar(row['Source Airport Name'],row['Source Airport Latitude'],row['Source Airport Longitude'])
