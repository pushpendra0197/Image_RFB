import numpy as np
import pandas as pd
import cv2
from cv2 import INTER_AREA
import streamlit as st
from PIL import Image
st.title("Image Resizer by PD")
st.warning("One Funtion at a time")
width=st.text_input("choose width")
height=st.text_input("choose height")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
flip_input=st.selectbox("choose Flip",["Left to Right & Right to Left","Up to Down & Down to Up","Both"])
left_column,middle_column, right_column,rightmost_column = st.columns(4,gap="small")
button=left_column.button("Resize",icon="📷")
button1=middle_column.button("Flip",icon="📷")
button2=right_column.button("Blurr",icon="📷")
button3=rightmost_column.button("Rotate",icon="📷")
angle_input=st.selectbox("choose angle",["Rotate90clock","Rotate180clock","Rotate90anticlock"])

if button:
    # Check if the file is uploaded
    if uploaded_file:
        try:
            # Open the image using PIL
            img = Image.open(uploaded_file)
            img_np = np.array(img)

            # Check if width and height are valid numbers
            if not width.isdigit() or not height.isdigit():
                st.error("Width and Height must be valid numbers.")
            else:
                width = int(width)
                height = int(height)

                # Ensure width and height are greater than 0
                if width <= 0 or height <= 0:
                    st.error("Width and Height must be greater than 0.")
                else:
                    # Resize the image
                    resize_img = cv2.resize(img_np, (width, height), interpolation=INTER_AREA)
                    
                    # Display resized image
                    st.image(resize_img, caption="Resized Image")
        except:
            st.error("something is wrong")
if button1:
    # Check if the file is uploaded
    if uploaded_file:
        try:
            # Open the image using PIL
            flip_img = Image.open(uploaded_file)
            Flip_np = np.array(flip_img)
            if flip_input=="Left to Right & Right to Left":
                flip_type=int(1)
            elif flip_input=="Up to Down & Down to Up":
                flip_type=int(0)
            elif flip_input=="Both":
                flip_type=int(-1)
            flip=cv2.flip(Flip_np,flip_type)
            st.image(flip, caption="Flipped image")
        except:
            st.error("something is wrong")
if button2:
    # Check if the file is uploaded
    if uploaded_file:
        try:
            # Open the image using PIL
            blurr_img = Image.open(uploaded_file)
            blurr_np = np.array(blurr_img)
            Blurr_img=cv2.GaussianBlur(blurr_np,(5,5),0)
            st.image(Blurr_img,caption="Blurr Image")
            
        except:
            st.error("something is wrong")
if button3:
    # Check if the file is uploaded
    if uploaded_file:
        try:
            # Open the image using PIL
            Rimge = Image.open(uploaded_file)
            rimge_np = np.array(Rimge)
            if angle_input=="Rotate90clock":
                angle_input=cv2.ROTATE_90_CLOCKWISE
            elif angle_input=="Rotate180clock":
                angle_input=cv2.ROTATE_180
            elif angle_input=="Rotate90anticlock":
                angle_input=cv2.ROTATE_90_COUNTERCLOCKWISE
            rotate=cv2.rotate(rimge_np,angle_input)
            st.image(image=rotate)
        
        except:
            st.error("Check angle or something is wrong")