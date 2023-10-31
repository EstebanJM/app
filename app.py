import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

DT = pd.read_csv('DataFrameDT.csv')

gdp_und = px.scatter(DT, x="Year", y="undernourishment", size = 'gdp', color="Country", title= 'RELACIÓN POR PAÍS ENTRE EL GPD Y LA DESNUTRICIÓN POR AÑO')
gdp_unem = px.scatter(DT, x="Year", y="unemployment", size = 'gdp' , color="Country", title= 'RELACIÓN POR PAÍS ENTRE EL GPD Y EL DESEMPLEO POR AÑO')
gdp_co2 = px.scatter(DT, x="Year", y="co2",size = 'gdp',  color="Country", title= 'RELACIÓN POR PAÍS EMTRE EL GPD Y EMISIÓN DE C02 POR AÑO')

south = DT[DT['Country'].isin(['Argentina', 'Uruguay', 'Chile', 'Peru', 'Brazil', 'Ecuador', 'Colombia', 'Paraguay', 'Bolivia', 'Venezuela, RB' ])]
north = DT[DT['Country'].isin(['Canada', 'United States', 'Costa Rica', 'Mexico'])]

variables = ['gdp', 'undernourishment', 'expectancy', 'co2', 'unemployment']
for variable in variables:
  LS1 = south.groupby('Year')[[variable]].mean()
  LN1 = north.groupby('Year')[[variable]].mean()

DE =plt.figure(figsize=(15, 5))

plt.plot(LS1.index, LS1[variable], label=f'{variable} Sudamérica', color='green', linewidth=2, linestyle='dashed')
plt.plot(LN1.index, LN1[variable], label=f'{variable} Norte América', color='blue', linewidth=2, linestyle='dashed')

plt.xlabel('Año')
plt.ylabel(f'Promedio de {variable}')
plt.title(f'PROMEDIO ANUAL DE {variable} EN SUR AMERICA Y NORTE AMERICA')
plt.legend()
plt.grid(linestyle='-', linewidth=0.5)




st.title("Medición del bienestar")


tab1, tab2, tab3, tab4  = st.tabs(["Analisis Grafico - Estadistico", "Analisis de Hipotesis", "Analisis Georreferenciado", "Integrantes"])

with tab1:

    st.subheader("Resumen e Interpretación Grafica - Estadistica")
    st.dataframe(DT.describe())
    st.write("---")
    st.plotly_chart(gdp_und)
    st.plotly_chart(gdp_unem)
    st.plotly_chart(gdp_co2)

    st.pyplot(DE)
    st.image("expe.png", use_column_width=True)
    st.image("co2.png", use_column_width=True)
    st.image("undern.png", use_column_width=True)
    st.image("gdp.png", use_column_width=True)

    st.write("---")

    st.write("Respecto a indicadores como el GDP per cápita o desnutrición, los niveles de Colombia son bajos en contraposición a los de países de norteamérica y estando en la media respecto a los países de sudamérica ")
    st.write("Colombia es el país de la región que tiene los mayores niveles de desempleo, incluso por encima de países como Argentina, Uruguay o Chile.")
    st.write("En cuanto a los niveles de CO2, la República de Colombia tiene unos buenos números en comparación de países como Estados Unidos, México o Canadá, los cuales alcanzan niveles de CO2 por encima del 4% y que incluso podrían sobrepasar el 17%")
    st.write("En general, los números de Norteamérica respecto a las variables que pueden explicar el bienestar son más alentadores respecto a los de sudamérica, a excepción de los niveles de CO2.")
    st.write("Se puede evidenciar que existe una relación directa entre el GDP per cápita y los niveles de CO2, donde entre más alto la primera variable, también lo será la segunda, como lo explican países como Estados Unidos o Canadá al ser más industrializados")


with tab2:

  st.subheader("Prueba de Hipotesis")

  Formula = r"H_0:  \text{No hay diferencia significativa entre Colombia y suramerica}"
  Formula += r", \\ H_1: \text{Existe una diferencia significativa entre Colombia y suramerica}"
  st.latex(Formula)

  st.write("Respecto a los resultados de las pruebas de hipótesis de Colombia y suramerica, se puede concluir que para las variables GDP, desnutrición y esperanza de vida, no hay diferencias estadísticamente significativas al ser su p-valor mayor a 0.05. En contraposición a las variables de CO2 y desempleo, en donde se evidencian un p-valor muy pequeño, lo que quiere decir que entre Colombia y el resto de la región sí existen diferencias significativas.")


  Formula = r"H_0:  \text{No hay diferencia significativa en las entre Colombia y Mexico}"
  Formula += r", \\ H_1: \text{Existe una diferencia significativa en las entre Colombia y Mexico}"
  st.latex(Formula)

  st.write("En las pruebas entre Colombia y México se ha encontrado que las variables GDP, desnutrición , emisión de CO2 y desempleo muestran diferencias estadísticamente significativas entre los grupos o condiciones evaluados. Esto indica que existen diferencias significativas en el Producto Interno Bruto, la prevalencia de la desnutrición, las emisiones de CO2 y las tasas de desempleo entre los grupos. Por otro lado, no se encontraron diferencias significativas en la esperanza de vida al nacer.")

  Formula = r"H_0:  \text{No hay diferencia significativa entre Colombia y Estados Unidos}"
  Formula += r", \\ H_1: \text{Existe una diferencia significativa entre Colombia y Estados Unidos}"
  st.latex(Formula)

  st.write("Para el análisis entre Colombia y EE.UU y de igual modo, entre Colombia y Canadá, se ha encontrado que todas las variables (GDP, desnutrición, esperanza de vida, emisión de CO2 y desempleo) muestran diferencias estadísticamente significativas entre los grupos o condiciones evaluados. Estos resultados indican que existen diferencias significativas en estas variables entre los grupos.")

  Formula = r"H_0:  \text{No hay diferencia significativa entre Colombia y Costa Rica}"
  Formula += r", \\ H_1: \text{Existe una diferencia significativa entre Colombia y Costa Rica}"
  st.latex(Formula)

  st.write("En cuanto a las pruebas de hipótesis entre Colombia y Costa Rica, se observó que las variables GDP, desnutrición, esperanza de vida y desempleo muestran diferencias estadísticamente significativas entre los grupos o condiciones evaluados. Esto sugiere que existen diferencias significativas en estas variables entre los grupos. Sin embargo, no se encontraron diferencias significativas en las emisiones de CO2 entre los grupos.")

with tab3:

  st.subheader("Mapas Georreferenciados")

  st.image("MAPA GENERAL.png", use_column_width=True)
  st.image("rey.png", use_column_width=True)
  st.image("reina.png", use_column_width=True)
  st.image("general.png", use_column_width=True)

with tab4:

  st.title("Integrantes")
  st.write("---")

  st.subheader("Michael Esteban Jimenez Medina")
  st.subheader("Diego Johan Lopez Fonseca")
  st.subheader("David Hernández Sicachá")