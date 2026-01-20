import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados de una aplicación.")

empleados = pd.read_csv("./resources/employees.csv")
st.divider()

with st.container(horizontal=True, vertical_alignment="center", gap="large"):
    color = st.color_picker("Elige un color para las barras", value="#3475B3")
    nombre_mostrar = st.toggle("Mostrar el nombre", value=True)
    sueldo_mostrar = st.toggle("Mostrar el sueldo de la barra")
    
fig, ax = plt.subplots()

barh = ax.barh(empleados["full name"], width=empleados["salary"], color=color)
ax.set_xlim(0., 4500.)

# Configuracion de los ejes
ax.get_yaxis().set_visible(nombre_mostrar)

if sueldo_mostrar:
    for bar in barh:
        width = bar.get_width()
        ax.text(
            width + 20.,                             
            bar.get_y() + bar.get_height() / 2, 
             f'{width}€',                        
            va='center',
            ha='left'
        )

st.pyplot(fig)

st.write("© Ismael Sihammou Anahnah - CPIFP Alan Turing")