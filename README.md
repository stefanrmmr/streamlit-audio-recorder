# Streamlit Audio Recorder

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://audiorecorder.streamlit.app/)
[![PyPI Latest Release](https://img.shields.io/pypi/v/streamlit-audiorec.svg)](https://pypi.org/project/streamlit-audiorec/) 

Custom component, implemented by [Stefan Rummer](https://www.linkedin.com/in/stefanrmmr/), <br/>
based on [doppelgunner](https://github.com/doppelgunner/audio-react-recorder/) 's [Audio-React-Recorder](https://www.npmjs.com/package/audio-react-recorder/) <br/>

![Screenshot 2022-05-16 at 16 58 36](https://user-images.githubusercontent.com/82606558/168626886-de128ffa-a3fe-422f-a748-395c29fa42f9.png) <br/>

## Features & Outlook
- Manage access to the user's microphone via the **browser's Media-API**
- Record, playback and revert audio-recordings in apps **deployed to the web**
- Download the final recording to your local system! - **WAV, 16 bit, 44.1 kHz**
- Directly return audio recording-data to Python backend! - **arrayBuffer format**<br>

## Component Setup & Usage Guide
**1.** PIP Install the component (download from PyPI)
```
pip install streamlit-audiorec
```
**2.** Import and Initialize the component (at the top of your script)
```
from st_audiorec import streamlit_audio_recorder
```

**3.** Add an Instance of the audio recorder to your streamlit app's code.
```
wav_audio_data = streamlit_audio_recorder()

if wav_audio_data is not None:
    # display audio data as received on the backend
    st.audio(wav_audio_data, format='audio/wav')
    
# INFO: by calling the function an instance of the audio recorder is created
# INFO: once a recording is completed, audio data will be saved to wav_audio_data
```
**4. Enjoy recording audio inside your streamlit app! 🎈**

Feel free to reach out to me in case you have any questions! <br>
Pls consider leaving a `star` ☆ with this repository to show your support.
