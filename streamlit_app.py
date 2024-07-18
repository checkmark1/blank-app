import streamlit as st
import csv
import statistics
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import random

def bar(color1, data):
    p = data
    x = range(4)
    plt.title("Colors and Numbers")
    plt.bar(x, p, color=color1)
    return plt

st.title('Bar Chart')
st.sidebar.header('Inputs')

value1 = st.sidebar.slider("Value 1",1,50)
value2 = st.sidebar.slider("Value 2",1,50)
value3 = st.sidebar.slider("Value 3",1,50)
value4 = st.sidebar.slider("Value 4",1,50)

data = [value1, value2, value3, value4]

colors = {"red":"r","green":"g","yellow":"y","blue":"b","cyan":"c"}
color_names = list(colors.keys())

color1 = st.sidebar.radio('Color:', color_names)

st.pyplot(bar(colors[color1], data))
st.sidebar.table(data)
if st.sidebar.button("Press Me"):
    st.balloons()
