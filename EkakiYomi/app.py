import streamlit as st
from streamlit_drawable_canvas import st_canvas
import cv2
import matplotlib.pyplot as plt
import bunkaron
from PIL import Image
import random
import glob

st.set_page_config(
    page_title="EkakiYomi.bandare", 
    page_icon="home.png")
backgroundColor="#FBF7F3"

if 'flag' not in st.session_state:
  st.session_state["flag"] = 0
if 'getwaka' not in st.session_state:
  st.session_state.getwaka=bunkaron.randwaka()



st.image("img/title.png")
if st.button("違う歌にする", key=1):
  st.session_state.getwaka=bunkaron.randwaka()
st.markdown(st.session_state.getwaka[0][1]+"　　"+st.session_state.getwaka[0][0])
st.sidebar.image("img/logo.png")
st.sidebar.image("img/title.png")

# Specify brush parameters and drawing mode
b_width = st.sidebar.slider("ペンのサイズ: ", 1, 100, 5)
b_color = st.sidebar.color_picker("ペンの色: ")

# Create a canvas component
canvas_result  = st_canvas(
#fill_color="rgba(255, 165, 0, 0.3)",
stroke_width=b_width,
stroke_color=b_color,
background_color="White",
width = 700,
height= 500,
key="canvas",
)


if st.button("投稿", key=0):
  st.session_state["flag"] = 1
if canvas_result.image_data is not None and st.session_state["flag"]==1:
 srcimg=canvas_result.image_data
 height, width, channels = srcimg.shape[:3]
 convimg=srcimg
 Image.fromarray(convimg).save('./data/'+str(st.session_state.getwaka[1])+'/'+str(random.randint(0,10000000))+'.png', 'PNG')
st.header('みんなの絵')
path = './data/'+str(st.session_state.getwaka[1])+'/*.png'
flist = glob.glob(path)
for file in flist:
  st.image(file)
st.session_state["flag"]=0
