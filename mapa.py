import pandas as pd
import folium as fl
from folium.plugins import MarkerCluster
import os
import webbrowser as wb
from MapaClass import *

df = pd.read_csv("./data/flights_final.csv")

def generador_mapa():
    

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

def generadorLineasMapa(Lineas,nombres):

    #Para ubicar el mapa a partir de una coordenada
    latitudMedia = df['Source Airport Latitude'].mean()
    longitudMedia = df['Source Airport Longitude'].mean()

    mapa = fl.Map(location=[latitudMedia,longitudMedia],zoom_start=3)


    #agrupar coordenadas cuando se esta alejado

    marker_cluster = MarkerCluster().add_to(mapa)

    for i in range (len(Lineas)):
            
            fl.Marker(
            location= Lineas[i],
            popup=f"<b>{nombres[i]}</b>",
            tooltip= f"{nombres[i]}",
            icon = fl.Icon(color='blue', icon='plane')   

            ).add_to(marker_cluster)

            if(i<len(Lineas)-1):
                fl.PolyLine(
                    locations=[Lineas[i],Lineas[i+1]],
                    color="yellow",
                    opacity=1

                ).add_to(marker_cluster)
    if os.path.exists("./Archivo mapa/MapaConecciones.html"):
        os.remove("./Archivo mapa/MapaConecciones.html")
    
    mapa_file="MapaConecciones.html"
    directorio =os.path.abspath("./Archivo mapa/")
    mapa.save(os.path.join(directorio,mapa_file))
    wb.open(os.path.join(directorio,mapa_file))









