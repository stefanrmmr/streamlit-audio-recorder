# streamlit_audio_recorder (Custom Component)

Implemented by [Stefan Rummer](https://www.linkedin.com/in/stefanrmmr/) - (work in progress)<br/>
Based on [doppelgunner](https://github.com/doppelgunner/audio-react-recorder)'s [Audio-React-Recorder](https://www.npmjs.com/package/audio-react-recorder)<br/>

![Screenshot 2022-05-16 at 16 58 36](https://user-images.githubusercontent.com/82606558/168626886-de128ffa-a3fe-422f-a748-395c29fa42f9.png)<br/>

## Features & Outlook
- Managing access to your microphone via the browser's Media-API
- Record, playback and revert audio-captures within the streamlit app
- Download the final recording to your local system (WAV, 16 bit, 44.1 kHz)
- Directly return audio recording-data to Python backend! (arrayBuffer)<br><br>
- **NEW:** Reduced repo size by removal of redundant node-modules! (393Mb --> 70Mb)
- **NEW:** Simplified SETUP TUTORIAL, that will get you to record audio within no time!


## Component Setup - step by step
**1.** Import and install relevant libraries to your Python project. 
```
import os
import numpy as np
import streamlit as st
from io import BytesIO
import streamlit.components.v1 as components
```
**2.** Add the folder `/st_audiorec` to the top level directory of your project.<br><br>
**3.** Add the file `st_custom_components.py` to your project wherever you like.<br><br>
**4.** Import the function `st_audiorec()` to your main streamlit application code.
```
from st_custom_components import st_audiorec
```
**5.** Add an instance of the audio recorder component to your streamlit app's code.
```
wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    # display audio data as received on the backend
    st.audio(wav_audio_data, format='audio/wav')
    
# INFO: by calling the function an instance of the audio recorder is created
# INFO: once a recording is completed, audio data will be saved to wav_audio_data
```
**6. Enjoy recording audio inside your streamlit app! 🎈**

Feel free to reach out to me in case you have any questions! <br>
Pls consider leaving a `star` ☆ with this repository to show your support.
