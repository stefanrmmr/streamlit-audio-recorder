# streamlit_audio_recorder (Custom Component)

Implemented by [Stefan Rummer](https://www.linkedin.com/in/stefanrmmr/) - (work in progress)<br/>
Based on [doppelgunner](https://github.com/doppelgunner/audio-react-recorder)'s [Audio-React-Recorder](https://www.npmjs.com/package/audio-react-recorder)<br/>

![Screenshot 2022-05-16 at 16 58 36](https://user-images.githubusercontent.com/82606558/168626886-de128ffa-a3fe-422f-a748-395c29fa42f9.png)<br/>

## Features & Outlook
- Managing access to your microphone via the browser's Media-API
- Record, playback and revert audio-captures within the streamlit app
- Download the final recording to your local system (WAV, 16bit, 44kHz)
- **NEW:** Directly return audio recording-data to Python backend! (arrayBuffer)


## Component Setup - step by step
1. Copy the folder "st_audiorec" to the top level directory of your streamlit project
2. Import "os", "streamlit as st" and "streamlit.components.v1 as components"
```
import os
import streamlit as st
import streamlit.components.v1 as components
```
3. Initialize path variables and declare the custom component using the given name
```
parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
st_audiorec = components.declare_component("st_audiorec", path=build_dir)
```
4. Create an instance of "streamlit-audio-recorder" and record client audio data! 🎈<br/>

```
st_audiorec()
```
