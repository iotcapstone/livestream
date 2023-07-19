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
st.image("https://plus.unsplash.com/premium_photo-1688045802023-60a42a082776?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80")
st.video("https://youtu.be/yVV_t_Tewvs")
