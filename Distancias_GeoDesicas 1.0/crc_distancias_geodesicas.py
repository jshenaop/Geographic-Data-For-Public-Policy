# -*- coding: utf-8 -*-
# Desarrollador Juan Sebastian Henao - Comisión Regulación Telecomunicaciones

import googlemaps
import json
import pandas as pd
import numpy as np
from geopy.distance import distance as geopy_distance
import csv
import datetime

##### Traer datos de Excel #####

df_municipios = pd.read_csv('municipios_gis.csv', sep=',', parse_dates=[0], header=0)
df_principales = pd.read_csv('principales_gis.csv', sep=',', parse_dates=[0], header=0)

municipios_cvs = df_municipios.ix[:,1]
lat_municipios_cvs    = df_municipios.ix[:,4]
long_municipios_cvs   = df_municipios.ix[:,5]

lista_municipios    = municipios_cvs.tolist()
lista_municipios_lat       = lat_municipios_cvs.tolist()
lista_municipios_long      = long_municipios_cvs.tolist()

pricipales_cvs = df_principales.ix[:,1]

lat_principales_cvs    = df_principales.ix[:,4]
long_principales_cvs   = df_principales.ix[:,5]

lista_principales    = pricipales_cvs.tolist()
lista_principales_lat       = lat_principales_cvs.tolist()
lista_principales_long      = long_principales_cvs.tolist()

##### Encuentra latitud del sitio buscado #####
# geocode_resultado = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# print geocode_resultado

##### Encuentra distancia de ruta entre dos ciudades #####
#orig_coord = (4.59,-74.07)
#dest_coord = (6.23,-75.57)

def distancia_ruta_google_maps(orig_coord,dest_coord):

    try:
        print orig_coord
        print dest_coord
        distancia_completa = gmaps.distance_matrix(orig_coord,dest_coord)
        print distancia_completa
        distancia = distancia_completa['rows'][0]['elements'][0]['distance']['value']/1000

    except:
        return "NO DISPONIBLE"

    return distancia


matriz_distacia = []

for municipio in lista_municipios:

    lista_distancia = []

    for principal in lista_principales:

        indice_principal = lista_principales.index(principal)
        indice_municipio = lista_municipios.index(municipio)

        orig_coord = (lista_principales_lat[indice_principal],lista_principales_long[indice_principal])
        dest_coord = (lista_municipios_lat[indice_municipio],lista_municipios_long[indice_municipio])
        distancia = d = geopy_distance(orig_coord, dest_coord)
        lista_distancia.append(distancia.kilometers)

    matriz_distacia.append(lista_distancia)

print matriz_distacia

#date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")

#nombre_archivo = date_string + str(columna_hoy) + "archivo.csv"

np.savetxt('Columna REPLACE.csv',matriz_distacia, delimiter=",", fmt="%s")

#with open('CLASS-' + date_string +'.csv', 'wb') as f:
#    writer = csv.writer(f)
#    writer.writerows(izip(matriz_distacia))
