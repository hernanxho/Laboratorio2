import tkinter as tk
from tkinter import messagebox
import mapa as m
from typing import Any
from Graph import *

coordenadas =[]
nombres = []
class GuiClass :

    
    
    def __init__(self):
        self.gui = tk.Tk()
        self.gui.geometry("1500x770")
        self.gui.title("gg")

        self.optionFrame= tk.Frame(self.gui,bg="#D2B48C")
        self.optionFrame.pack(side=tk.LEFT)
        self.optionFrame.pack_propagate(False)
        self.optionFrame.configure(width=300, height=770)

        self.mainFrame = tk.Frame(self.gui, bg="#FFFAF0", highlightbackground="black", highlightthickness=2)
        self.mainFrame.pack(fill=tk.BOTH, expand=True)

        self.efecto = tk.Label(self.optionFrame,text="",bg="#D2B48C")
        self.efecto.place(x = 30, y = 80,height=80,width=10)

        self.generadorMapa = tk.Button(text="Generador del Mapa",bg="#CD853F",font = ("Bold", 15), command = lambda: self.generar_mapa())
        self.generadorMapa.place(x = 40, y = 80,height=80,width=220)

        self.info_grafo = tk.Button(text="Informacion del Grafo",bg="#CD853F",font = ("Bold", 15), command= lambda: self.info())
        self.info_grafo.place(x = 40, y = 200,height=80,width=220)

        self.pesoGrafo = tk.Button(text="Peso del arbol de \n expansión mínima",bg="#CD853F",font = ("Bold", 15),command= lambda: self.peso())
        self.pesoGrafo.place(x = 40, y = 310,height=80,width=220)

        self.codigoVertice = tk.Button(text="Vértice",bg="#CD853F",font = ("Bold", 15), command= lambda: self.codigo())
        self.codigoVertice.place(x = 40, y = 430,height=80,width=220)





        self.gui.mainloop()
    
    def startFrame(self,x,y):
            self.efecto.config(bg="#F5F5F5")   
            self.efecto.place(x=x,y=y,height=80,width=10)
    def deletesFrame(self,lb):
        for frame in lb.winfo_children():
            frame.destroy()
    
    def generar_mapa(self):
            self.startFrame(30,80)
            m.generador_mapa()
    def peso(self):
          self.deletesFrame(self.mainFrame)
          self.startFrame(30,310)
          self.Peso=tk.Frame(self.mainFrame, bg="#FFFACD", highlightbackground="black", highlightthickness=2)
          self.Peso.place(x=0, y=0, width=1196, height=767)

          self.Titulo = tk.Label(self.Peso, text = "PESO \n  GRAFO", highlightbackground="black", highlightthickness=2, font = ("Bold", 30) )
          self.Titulo.place(x=1196 / 2, y=100, width= 500, height = 100,  anchor=tk.CENTER)

          pesos = g.mst_weight_per_component()
          peso_total = 0
          for i in  range(1,8):
                peso_total += pesos[i]     

          print(pesos)
          ms = "El peso total de los arbol de expansión mínima es:    " + str(peso_total)+ "\nEl peso del componente #1 del arbol de expansión mínima es: " +  str(pesos[1]) + "\nEl peso del componente #2 del arbol de  expansión mínima es: " +  str(pesos[2]) + "\nEl peso  del componente #3 del arbol de expansión mínima es: " +  str(pesos [3]) + "\nEl peso del componente #4 del arbol de expansión mínima  es: " +  str(pesos[4]) + "\nEl peso del componente #5  del arbol de expansión mínima es: " +  str(pesos[5]) +  "\nEl peso del componente #6 del arbol de expansión mínima es: " +    str(pesos[6]) + "\nEl peso del componente #7 del arbol  de expansión mínima es: " +  str(pesos[7]) 

          self.weight = tk.Label(self.Peso, text = ""+ ms, highlightbackground="black", highlightthickness=2, font = ("Arial", 19) )
          self.weight.place(x=1196 / 2, y=450, width= 1000, height = 500,  anchor=tk.CENTER)
    
    def info(self):
          self.deletesFrame(self.mainFrame)
          self.startFrame(30,200)
          self.Info=tk.Frame(self.mainFrame, bg="#FFFACD", highlightbackground="black", highlightthickness=2)
          self.Info.place(x=0, y=0, width=1196, height=767)   

          self.Titulo = tk.Label(self.Info, text = "INFORMACIÓN \n  GRAFO", highlightbackground="black", highlightthickness=2, font = ("Bold", 30) )
          self.Titulo.place(x=1196 / 2, y=100, width= 500, height = 100,  anchor=tk.CENTER)

          ms = "¿El grafo es conexo?:    " + str(conection)+ "\nEl numero de vértices del grafo es: " + str(g.n)  + "\nEl numero de componentes son:   " + str(len(n_components)) + "\nEl numero de vertices en el componente #1:   " +  str(len(n_components[0])) + "\nEl numero de vertices en el componente #2:    "  + str(len(n_components[1])) + "\nEl numero de vertices en el componente #3:   "  + str(len(n_components[2])) + "\nEl numero de vertices en el componente #4:    "  + str(len(n_components[3])) + "\nEl numero de vertices en el componente #5:   "  + str(len(n_components[4])) + "\nEl numero de vertices en el componente #6:    "  + str(len(n_components[5])) + "\nEl numero de vertices en el componente #7:   "  + str(len (n_components[6]))

          self.informacion = tk.Label(self.Info, text = ""+ ms, highlightbackground="black", highlightthickness=2, font = ("Arial", 19) )
          self.informacion.place(x=1196 / 2, y=450, width= 800, height = 500,  anchor=tk.CENTER)

    
    def codigo(self):
          
          self.deletesFrame(self.mainFrame)
          self.startFrame(30,430)
          
          self.Codigo=tk.Frame(self.mainFrame, bg="#FFFACD", highlightbackground="black", highlightthickness=2)
          self.Codigo.place(x=0, y=0, width=1196, height=767)
          
          self.codigotext = tk.Entry(self.Codigo,width=30, font=("Arial",40))
          self.codigotext.place(x=160,y=200)
          
          self.infoAereopuerto=tk.Button(self.Codigo,text="Informacion \n aereopuerto",font = ("Bold", 15), command=lambda:self.mostrar_aeropuerto(self.codigotext.get()))
          self.infoAereopuerto.place(x=160,y=400,height=80,width=200)
          
          self.infoCaminosAereopuertos=tk.Button(self.Codigo,text="Caminos \n aereopuertos",font = ("Bold", 15),  command=lambda:self.mostrar_caminos_aeropuertos(self.codigotext.get()))

          self.infoCaminosAereopuertos.place(x=510,y=400,height=80,width=200)
          
          self.segundoCodigo = tk.Button(self.Codigo, text="Segundo vertice" ,font = ("Bold", 15), command= lambda: self.mostrarEntrada())
          self.segundoCodigo.place(x=850,y=400,height=80,width=200)

          self.codigotext2 = tk.Entry(self.Codigo,width=30, font=("Arial",40))
          self.codigotext2.place_forget()

          self.mostrarCamino=tk.Button(self.Codigo,text="Mostar Camino \n minimo",font = ("Bold", 15), command= lambda: self.findMinPath(self.codigotext.get().strip(),self.codigotext2.get().strip()))
          self.mostrarCamino.place_forget()

          
    def  mostrar_aeropuerto(self, code):
          ms = g.obtener_info(str(code))
          if ms == "Airport code does not exist.":
                self.informacion = messagebox.showinfo("INFO", "No existe")
          else:
                self.informacion = messagebox.showinfo("INFO", "La información del aeropuerto con el codigo " + ms["code"]  + " es:\n" + "Nombre: " + ms["name"] + "\nLatitud: " + str(ms["latitude"]) + "\nLongitud: " + str(ms["longitude"]) + "\nPais: " + ms["country"]+ "\nCiudad: " + ms["city"])


    
    def mostrarEntrada(self):
          self.mostrarCamino.place(x=510,y=600,height=80,width=200)
          self.codigotext2.place(x=160,y=300)

    def mostrar_caminos_aeropuertos(self,code): #Los 10 maximos caminos minimos
            total_distances = g.Dijkstra(indexAirport[code])
            distances = [(node, value[0]) for node, value in total_distances.items()]
            distances.sort(key=lambda x: x[1], reverse=True)

            ten_distances = distances[:10]

            i=1
            ms ="#AEROPUERTO MAS ALEJADO\n\n"

            for node, distance in ten_distances:
                  ms += (f"#{i}: Nombre: {g.dataGraph[node]['name']}, "
                        f"Codigo: {g.dataGraph[node]['code']}, "
                        f"Latitud: {g.dataGraph[node]['latitude']}, "
                        f"Longitud: {g.dataGraph[node]['longitude']}, "
                        f"Pais: {g.dataGraph[node]['country']}, "
                        f"Ciudad: {g.dataGraph[node]['city']}, "
                        f"Distancia {g.dataGraph[indexAirport[code]]['name']}: {distance}\n\n")
                  i+=1
            self.ten_label = messagebox.showinfo("10 aeropuertos mas alejados", ms)

    def findMinPath(self, v1, v2): #El min path entre v1 y v2
          paths =  g.Dijkstra(indexAirport[v1])
          print(paths)
          i=1
          ms ="#AEROPUERTOS DEL CAMINO MINIMO\n\n"
          try:
            if indexAirport[v2] in paths:
                  for airport in paths[indexAirport[v2]][1]:
                              ms += (f"#{i}: Nombre: {g.dataGraph[airport]['name']}, "
                                    f"Codigo: {g.dataGraph[airport]['code']}, "
                                    f"Latitud: {g.dataGraph[airport]['latitude']}, "
                                    f"Longitud: {g.dataGraph[airport]['longitude']}, "
                                    f"Pais: {g.dataGraph[airport]['country']}, "
                                    f"Ciudad: {g.dataGraph[airport]['city']}\n\n")
                              coordenadas.append((g.dataGraph[airport]['latitude'],g.dataGraph[airport]['longitude']))
                              nombres.append(g.dataGraph[airport]['name'])
                              i+=1
                  m.generadorLineasMapa(coordenadas,nombres)
                  self.minAirports = messagebox.showinfo("Camino  minimo", ms)

                  print(coordenadas)
            
            
          except Exception as e:
            self.minAirports = messagebox.showerror("ERROR", "NO HAY CAMINO")


          

              

GuiClass()
