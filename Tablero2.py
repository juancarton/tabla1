#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd

# Autenticación simple
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Usuario:")
    password = st.text_input("Contraseña:", type="password")
    if st.button("Iniciar sesión"):
        if username == "ileana" and password == "reyes":  # Cambia esto por credenciales más seguras
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos")
else:
    st.title("Registro comparativo diario de venta de los 2 clubes")
    
    # Cargar datos
    df = pd.read_excel('Tablero1.xlsx')
    st.write(df)
    
    # Botón para cerrar sesión
    if st.button("Cerrar sesión"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# In[ ]:



