import tkinter as tk
import geopandas as gpd
from geopandas.array import to_shapely
import matplotlib.pyplot as plt
import pandas
from skyfield.api import load, wgs84
from skyfield.functions import to_spherical
from skyfield.api import EarthSatellite
from PIL import ImageTk, Image

def mapeoRealTime():

    mapaMundo=gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    #se configurara el canvas en matplotlib
    #se crea un objeto axes

    fig,ax=plt.subplots(1,1,figsize=(10,8))
    mapaMundo.plot(ax=ax, alpha=0.4, color='grey')
    #mi ubicacion
    plt.plot(-99.23333,19.28333,marker="o",color="red",markersize=2)
    #***********************************************
    conta=0
    tle=open('iridium-33-debris.txt','r')
    while(True):
        linea=tle.readline()
        if len(linea)>30 :
            conta=conta+1
            if conta%2==0:
                t=linea
                #print(t)
                ts = load.timescale()
                satellite = EarthSatellite(s, t, 'o', ts)
                #print(satellite)
                #obtener fecha y hora actual
                t=ts.now()
                geocentric=satellite.at(t)
                #print(geocentric.position.km)
                subpoint=wgs84.subpoint(geocentric)
                #print('Latitude:', subpoint.latitude)
                #print('Longitude:', subpoint.longitude)
                plt.plot(subpoint.longitude.degrees,subpoint.latitude.degrees,marker="o",color="black",markersize=1)
            else:
                s=linea
                #print(s)
        if not linea:
            break

    tle.close()
    #*******************************************
    #***********************************************
    conta=0
    tle=open('cosmos-2251-debris.txt','r')
    while(True):
        linea=tle.readline()
        if len(linea)>30 :
            conta=conta+1
            if conta%2==0:
                t=linea
                #print(t)
                ts = load.timescale()
                satellite = EarthSatellite(s, t, 'o', ts)
                #print(satellite)
                #obtener fecha y hora actual
                t=ts.now()
                geocentric=satellite.at(t)
                #print(geocentric.position.km)
                subpoint=wgs84.subpoint(geocentric)
                #print('Latitude:', subpoint.latitude)
                #print('Longitude:', subpoint.longitude)
                plt.plot(subpoint.longitude.degrees,subpoint.latitude.degrees,marker="o",color="black",markersize=1)
            else:
                s=linea
                #print(s)
        if not linea:
            break

    tle.close()
    #*******************************************
    #***********************************************
    conta=0
    tle=open('2019-006.txt','r')
    while(True):
        linea=tle.readline()
        if len(linea)>30 :
            conta=conta+1
            if conta%2==0:
                t=linea
                #print(t)
                ts = load.timescale()
                satellite = EarthSatellite(s, t, 'o', ts)
                #print(satellite)
                #obtener fecha y hora actual
                t=ts.now()
                geocentric=satellite.at(t)
                #print(geocentric.position.km)
                subpoint=wgs84.subpoint(geocentric)
                #print('Latitude:', subpoint.latitude)
                #print('Longitude:', subpoint.longitude)
                plt.plot(subpoint.longitude.degrees,subpoint.latitude.degrees,marker="o",color="black",markersize=1)
            else:
                s=linea
                #print(s)
        if not linea:
            break

    tle.close()
    #*******************************************
    #***********************************************
    conta=0
    tle=open('1999-025.txt','r')
    while(True):
        linea=tle.readline()
        if len(linea)>30 :
            conta=conta+1
            if conta%2==0:
                t=linea
                #print(t)
                ts = load.timescale()
                satellite = EarthSatellite(s, t, 'o', ts)
                #print(satellite)
                #obtener fecha y hora actual
                t=ts.now()
                geocentric=satellite.at(t)
                #print(geocentric.position.km)
                subpoint=wgs84.subpoint(geocentric)
                #print('Latitude:', subpoint.latitude)
                #print('Longitude:', subpoint.longitude)
                plt.plot(subpoint.longitude.degrees,subpoint.latitude.degrees,marker="o",color="black",markersize=1)
            else:
                s=linea
                #print(s)
        if not linea:
            break

    tle.close()
    #*******************************************
    plt.show()






master = tk.Tk()
tk.Label(master, 
         text="Año").grid(row=0)
tk.Label(master, 
         text="Mes").grid(row=1)
tk.Label(master, 
         text="Dia").grid(row=2)
tk.Label(master, 
         text="Hora").grid(row=3)
tk.Label(master, 
         text="minuto").grid(row=4)
tk.Label(master, 
         text="Segundo").grid(row=5)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)

logo=Image.open('logo.png')
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=3,row=0)


def mapeoPorPedido():


    mapaMundo=gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    #se configurara el canvas en matplotlib
    #se crea un objeto axes

    fig,ax=plt.subplots(1,1,figsize=(10,8))
    mapaMundo.plot(ax=ax, alpha=0.4, color='grey')
    #mi ubicacion
    plt.plot(-99.23333,19.28333,marker="o",color="red",markersize=2)
    #***********************************************
    conta=0
    tle=open('iridium-33-debris.txt','r')
    while(True):
        linea=tle.readline()
        if len(linea)>30 :
            conta=conta+1
            if conta%2==0:
                t=linea
                #print(t)
                ts = load.timescale()
                satellite = EarthSatellite(s, t, 'o', ts)
                #print(satellite)
                #obtener fecha y hora actual
                t=ts.utc(int(e1.get()),int(e2.get()),int(e3.get()),int(e4.get()),int(e5.get()),int(e6.get()))
                geocentric=satellite.at(t)
                #print(geocentric.position.km)
                subpoint=wgs84.subpoint(geocentric)
                #print('Latitude:', subpoint.latitude)
                #print('Longitude:', subpoint.longitude)
                plt.plot(subpoint.longitude.degrees,subpoint.latitude.degrees,marker="o",color="black",markersize=1)
            else:
                s=linea
                #print(s)
        if not linea:
            break

    tle.close()
    #*******************************************
    #***********************************************
    conta=0
    tle=open('cosmos-2251-debris.txt','r')
    while(True):
        linea=tle.readline()
        if len(linea)>30 :
            conta=conta+1
            if conta%2==0:
                t=linea
                #print(t)
                ts = load.timescale()
                satellite = EarthSatellite(s, t, 'o', ts)
                #print(satellite)
                #obtener fecha y hora actual
                t=ts.now()
                geocentric=satellite.at(t)
                #print(geocentric.position.km)
                subpoint=wgs84.subpoint(geocentric)
                #print('Latitude:', subpoint.latitude)
                #print('Longitude:', subpoint.longitude)
                plt.plot(subpoint.longitude.degrees,subpoint.latitude.degrees,marker="o",color="black",markersize=1)
            else:
                s=linea
                #print(s)
        if not linea:
            break

    tle.close()
    #*******************************************
    #***********************************************
    conta=0
    tle=open('2019-006.txt','r')
    while(True):
        linea=tle.readline()
        if len(linea)>30 :
            conta=conta+1
            if conta%2==0:
                t=linea
                #print(t)
                ts = load.timescale()
                satellite = EarthSatellite(s, t, 'o', ts)
                #print(satellite)
                #obtener fecha y hora actual
                t=ts.now()
                geocentric=satellite.at(t)
                #print(geocentric.position.km)
                subpoint=wgs84.subpoint(geocentric)
                #print('Latitude:', subpoint.latitude)
                #print('Longitude:', subpoint.longitude)
                plt.plot(subpoint.longitude.degrees,subpoint.latitude.degrees,marker="o",color="black",markersize=1)
            else:
                s=linea
                #print(s)
        if not linea:
            break

    tle.close()
    #*******************************************
    #***********************************************
    conta=0
    tle=open('1999-025.txt','r')
    while(True):
        linea=tle.readline()
        if len(linea)>30 :
            conta=conta+1
            if conta%2==0:
                t=linea
                #print(t)
                ts = load.timescale()
                satellite = EarthSatellite(s, t, 'o', ts)
                #print(satellite)
                #obtener fecha y hora actual
                t=ts.now()
                geocentric=satellite.at(t)
                #print(geocentric.position.km)
                subpoint=wgs84.subpoint(geocentric)
                #print('Latitude:', subpoint.latitude)
                #print('Longitude:', subpoint.longitude)
                plt.plot(subpoint.longitude.degrees,subpoint.latitude.degrees,marker="o",color="black",markersize=1)
            else:
                s=linea
                #print(s)
        if not linea:
            break

    tle.close()
    #*******************************************
    plt.show()


tk.Button(master, 
          text='realTime', command=mapeoRealTime).grid(row=6, 
                                                       column=0, 
                                                       sticky=tk.W, 
                                                       pady=4)


tk.Button(master, 
          text='pedidoTime', command=mapeoPorPedido).grid(row=6, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
tk.Button(master, 
          text='Salir', 
          command=master.quit).grid(row=6, 
                                    column=2, 
                                    sticky=tk.W, 
                                    pady=4)
tk.mainloop()