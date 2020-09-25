import csv

Lista_datos= []
su=215691298000
#Llamador del archivo y creacion de lista de listas
with open ("synergy_logistics_database.csv","r")as archivo:
  lector = csv.reader (archivo)

  for linea in lector:
   Lista_datos.append(linea)

#Generar Rutas de Exportaciones, con contador(sorted) y sumador $
print ("Rutas de Exportacion  OPCION 1")
print ("-------------------------------------------------")
direccion= "Exports"
contador=0
rutas_contadas=[]
lista_conteo= []
sumador=0

for ruta in Lista_datos:
  if ruta [1]== direccion:
    ruta_actual=[ruta[2], ruta[3]]
    if ruta_actual not in rutas_contadas:
      for movimiento in Lista_datos:
        if ruta_actual == [movimiento [2],movimiento[3]]:
          contador+=1
          sumador+= int(movimiento[9])
      rutas_contadas.append(ruta_actual)
      lista_conteo.append([ruta[2],ruta[3],contador,sumador])
      contador=0
      sumador=0
     
lista_conteo.sort(reverse=True, key=lambda x:x[2])
for pais in lista_conteo:
  print(pais)

#Generar Rutas de Importaciones, con contador(sorted) y sumador $
print ("------------------------------------------------")
print ("Rutas de Importacion  OPCION 1")
print ("-------------------------------------------------")
direccion_2= "Imports"
contador=0
rutas_contadas=[]
lista_conteo= []
sumador=0

for ruta in Lista_datos:
  if ruta [1]== direccion_2:
    ruta_actual=[ruta[2], ruta[3]]
    if ruta_actual not in rutas_contadas:
      for movimiento in Lista_datos:
        if ruta_actual == [movimiento [2],movimiento[3]]:
          if movimiento [1]== direccion_2:
            contador+=1
            sumador+= int(movimiento[9])
      rutas_contadas.append(ruta_actual)
      lista_conteo.append([ruta[2],ruta[3],contador,sumador])
      contador=0
      sumador=0
     
lista_conteo.sort(reverse=True, key=lambda x:x[2])
for pais in lista_conteo:
  print(pais)

#Medios de Transporte con Valor en $
print ("------------------------------------------------")
print ("Medios de Transporte con su Valor en $  OPCION 2")
print ("-------------------------------------------------")
direccion_3= "Exports"
contador=0
medios_contados=[]
lista_conteo= []

for medio in Lista_datos:
  if medio [1]== direccion_3:
    ruta_actual=[medio[7]]
    if ruta_actual not in medios_contados:
      for movimiento in Lista_datos:
        if ruta_actual == [movimiento [7]]:
          contador+= int(movimiento[9])
      medios_contados.append(ruta_actual)
      lista_conteo.append([medio[7],contador])
      contador=0
     
lista_conteo.sort(reverse=True, key=lambda x:x[1])
for med in lista_conteo:
  print(med)

#Valor Total de Expotaciones e Importaciones por Pais, Porcentaje
print ("------------------------------------------------")
print ("Valor Total de Expotaciones e Importaciones por Pais, Porcentaje OPCION 3")
print ("-------------------------------------------------")
direccion= "Exports"
contador=0
rutas_contadas=[]
lista_conteo= []

for ruta in Lista_datos:
  if ruta [1]== direccion:
    ruta_actual=[ruta[2]]
    if ruta_actual not in rutas_contadas:
      for movimiento in Lista_datos:
        if ruta_actual == [movimiento [2]]:
          contador+= int(movimiento[9])
      rutas_contadas.append(ruta_actual)
      lista_conteo.append([ruta[2],contador,(contador/su)*100])
      contador=0
     
lista_conteo.sort(reverse=True, key=lambda x:x[1])
for pais in lista_conteo:
  print(pais)