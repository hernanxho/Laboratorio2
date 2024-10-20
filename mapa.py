import pandas as pd
import folium as fl
from folium.plugins import MarkerCluster
import os
import webbrowser as wb
from MapaClass import *



def generador_mapa():
    df = pd.read_csv("./data/flights_final.csv")

    #Instancia de la MapaClass
    mapainstancia = Mapa()
    mapainstancia.agregar()

    latitudMedia = df['Source Airport Latitude'].mean()
    longitudMedia = df['Source Airport Longitude'].mean()

    mapa = fl.Map(location=[latitudMedia,longitudMedia],zoom_start=3)

    marker_cluster = MarkerCluster().add_to(mapa)

    for aeropuerto in mapainstancia.aeropuertos:
        fl.Marker(
            location=[aeropuerto.latitude,aeropuerto.longitude],
            popup=f"<b>{aeropuerto.nombre}</b>",
            tooltip= f"{aeropuerto.nombre}",
            icon = fl.Icon(color='blue', icon='plane')
        ).add_to(marker_cluster)

    mapa_file="Mapa.html"
    directorio =os.path.abspath("./Archivo mapa/")
    mapa.save(os.path.join(directorio,mapa_file))
    wb.open(os.path.join(directorio,mapa_file))



