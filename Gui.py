import tkinter as tk
import mapa as m
from typing import Any

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
    
    def info(self):
          self.deletesFrame(self.mainFrame)
          self.startFrame(30,200)
          self.Info=tk.Frame(self.mainFrame, bg="#FFFACD", highlightbackground="black", highlightthickness=2)
          self.Info.place(x=0, y=0, width=1196, height=767)
    
    def codigo(self):
          
          self.deletesFrame(self.mainFrame)
          self.startFrame(30,430)
          
          self.Codigo=tk.Frame(self.mainFrame, bg="#FFFACD", highlightbackground="black", highlightthickness=2)
          self.Codigo.place(x=0, y=0, width=1196, height=767)
          
          self.codigotext = tk.Entry(self.Codigo,width=30, font=("Arial",40))
          self.codigotext.place(x=160,y=200)
          
          self.infoAereopuerto=tk.Button(self.Codigo,text="Informacion \n aereopuerto",font = ("Bold", 15))
          self.infoAereopuerto.place(x=160,y=400,height=80,width=200)
          
          self.infoCaminosAereopuertos=tk.Button(self.Codigo,text="Caminos \n aereopuertos",font = ("Bold", 15))
          self.infoCaminosAereopuertos.place(x=510,y=400,height=80,width=200)
          
          self.segundoCodigo = tk.Button(self.Codigo, text="Segundo vertice" ,font = ("Bold", 15), command= lambda: self.mostrarEntrada())
          self.segundoCodigo.place(x=850,y=400,height=80,width=200)

          self.codigotext2 = tk.Entry(self.Codigo,width=30, font=("Arial",40))
          self.codigotext2.place_forget()

          self.mostrarCamino=tk.Button(self.Codigo,text="Mostar Camino \n minimo",font = ("Bold", 15))
          self.mostrarCamino.place_forget()
    
    def mostrarEntrada(self):
          self.mostrarCamino.place(x=510,y=600,height=80,width=200)
          self.codigotext2.place(x=160,y=300)
              

GuiClass()
