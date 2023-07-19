#importing streamlit library

import streamlit as st



#displaying a local video file

#video_file = open('FILENAME', 'rb') #enter the filename with filepath

#video_bytes = video_file.read() #reading the file

#st.video(video_bytes) #displaying the video



#displaying a video by simply passing a Youtube link

f = open("test.txt", "wa")
f.write("Hello fuckers!\n")
f.close()
f = open("test.txt", "r")
content = f.read()
f.close()

st.text(conent)
st.video("https://youtu.be/yVV_t_Tewvs")
