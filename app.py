import streamlit as st
from PIL import Image

import cv2 
import color


Output_image = 256
newsize = (256,256)


def main():
    @st.cache
    def load_image(img):
        image = Image.open(img)
        image = image.convert('L')
        newsize = (256,256)
        image = image.resize(newsize)
        return image
    col1,col2=st.columns(2)
    #image = load_image('cover.png')
    img  = st.file_uploader('Upload an image',type=['jpg','png','jpeg'])
    if img is not None:
            image = Image.open(img)
            # image = image.convert('L')
            # img_convert = image.convert('L')
            img_convert = image.resize(newsize)
            with col1:
                st.image(img_convert,use_column_width=True,width=Output_image)
            print(type(img_convert))
         
            colorImg=color.colorize_image(img_convert)
            with col2:
                st.image(colorImg, use_column_width=True)

if __name__ == '__main__':
    main()
