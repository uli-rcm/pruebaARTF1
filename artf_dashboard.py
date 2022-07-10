# -*- coding: utf-8 -*-

'''
Genere un programa que tenga un menú en el cual el usuario pueda seleccionar 
entre dos opciones:

(1) Saludar: esta opción debe pedir el nombre al usuario y saludarlo.
(2) Tirar un dado: esta debe generar aleatoriamente un número y mostrarlo.
(3) Salir: esta opción debe terminar el programa.

'''

################ Importaciones ################
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #Para realizar gráficas

################ Funciones ################


################ Programa principal ################

st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

st.latex('\int_0^1 (x^2 + 1) \mathrm{d}x')

#Importación sin índice
df = pd.read_excel("Base_Publica_Carga_Ferrocarril.xlsx", sheet_name="Carga", engine='openpyxl') #Se importa el archivo

#######################Procesamiento preliminar#######################
#Columna adicional
df["t_millones"] = df["Toneladas (Neta)"]/1e6

# Se generan las categorías para los meses, de forma que queden ordenados
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] 
df['Mes'] = pd.Categorical(df['Mes'], categories=meses, ordered=True) #Se categoriza la columna "Mes", considerando que los meses están ordenados

#Filtro
filtro = (df["Año"] >= 2016) & (df["Año"] <= 2018)
df2 = df[filtro]

#Creación de la tabla dinámica (columnas, filas y valores)
df2 = df2.pivot_table(values="t_millones", index="Mes", columns="Año", aggfunc=np.sum, fill_value=0)

#######################Generación de la figura#######################
fig6 = plt.figure()

# Configurar parámetros generales de las gráficas
plt.rcParams.update({'font.size': 9})
plt.rcParams["figure.figsize"] = (16, 10) #Tamaño de las figuras; si se necesita, puede declararse antes de cada figura

plt.plot(df2.index,df2[2016], label=2016)
plt.plot(df2.index,df2[2017], label=2017)
plt.plot(df2.index,df2[2018], label=2018)

#Título de la gráfica
plt.title("Movimiento de toneladas netas")

#Etiquetas de los ejes
plt.xlabel("Mes")
plt.ylabel("Millones de toneladas netas")
plt.grid()

#Mostrar etiquetas de los datos
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=3)

#df
st.write("Encabezado del DataFrame completo:")
st.write(df.head())

st.write("Encabezado del DataFrame de la gráfica 1:")
st.write(df2)
st.pyplot(fig6)



#######################Procesamiento preliminar#######################
#Columna adicional
df["t_millones"] = df["Toneladas (Neta)"]/1e6

# Se generan las categorías para los meses, de forma que queden ordenados
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] 
df['Mes'] = pd.Categorical(df['Mes'], categories=meses, ordered=True) #Se categoriza la columna "Mes", considerando que los meses están ordenados

#Filtro
filtro = (df["Año"] >= 2016) & (df["Año"] <= 2018)
df2 = df[filtro]

#Creación de la tabla dinámica (columnas, filas y valores)
df2 = df2.pivot_table(values="t_millones", index="Mes", columns="Año", aggfunc=np.sum, fill_value=0)

#######################Generación de la figura#######################
fig7 = plt.figure()

# Configurar parámetros generales de las gráficas
plt.rcParams.update({'font.size': 9})
plt.rcParams["figure.figsize"] = (16, 10) #Tamaño de las figuras; si se necesita, puede declararse antes de cada figura

plt.bar(df2.index,df2[2016], label=2016)
plt.plot(df2.index,df2[2017], label=2017)
plt.plot(df2.index,df2[2018], label=2018)

#Título de la gráfica
plt.title("Movimiento de toneladas netas")

#Etiquetas de los ejes
plt.xlabel("Mes")
plt.ylabel("Millones de toneladas netas")
plt.grid()

#Mostrar etiquetas de los datos
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=3)

st.write("Encabezado del DataFrame de la gráfica 2:")
st.write(df2)
st.pyplot(fig7)