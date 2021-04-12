import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

DATE_COLUMN = "date/time"
RAD_TO_DEG = 57.2958

JOINT_DATA_URL = "https://raw.githubusercontent.com/david0429/ur_motion_streamlit/master/data/joints.csv"
CART_DATA_URL = "https://raw.githubusercontent.com/david0429/ur_motion_streamlit/master/data/cart.csv"

def get_j_dial(name, joint_data):
    return go.Figure(go.Indicator(
        value = -360,
        mode = "gauge",
        title = {'text': name},
        gauge = {'axis': {'range': [-360, 360]},
                 'steps' : [
                     {'range': [joint_data[name].min() * RAD_TO_DEG, joint_data[name].max() * RAD_TO_DEG], 'color': "teal", 'thickness': 0.8}],
                 }))

def load_data():
    cart_data = pd.read_csv(CART_DATA_URL)
    joint_data = pd.read_csv(JOINT_DATA_URL)

    cart_data[DATE_COLUMN] = pd.to_datetime(cart_data[DATE_COLUMN])
    joint_data[DATE_COLUMN] = pd.to_datetime(joint_data[DATE_COLUMN])
    return cart_data, joint_data

cart_data, joint_data = load_data()

path_fig = px.scatter_3d(cart_data, x='x', y='y', z='z')
st.plotly_chart(path_fig)

j1_fig = get_j_dial("j1", joint_data)
j2_fig = get_j_dial("j2", joint_data)
j3_fig = get_j_dial("j3", joint_data)
j4_fig = get_j_dial("j4", joint_data)
j5_fig = get_j_dial("j5", joint_data)
j6_fig = get_j_dial("j6", joint_data)

st.plotly_chart(j1_fig)
st.plotly_chart(j2_fig)
st.plotly_chart(j3_fig)
st.plotly_chart(j4_fig)
st.plotly_chart(j5_fig)
st.plotly_chart(j6_fig)
