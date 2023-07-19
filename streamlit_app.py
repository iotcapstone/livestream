#importing streamlit library

import streamlit as st
from PIL import Image


#displaying a local video file

#video_file = open('FILENAME', 'rb') #enter the filename with filepath

#video_bytes = video_file.read() #reading the file

#st.video(video_bytes) #displaying the video



#displaying a video by simply passing a Youtube link

f = open("test.txt", "a")
f.write("Hello fuckers!\n")
f.close()
f = open("test.txt", "r")
content = f.read()
f.close()


#p = Image.open("test_Printer001.jpg")


st.text(content)
st.image("https://en.wikipedia.org/wiki/Google_Images")
st.video("https://youtu.be/yVV_t_Tewvs")
