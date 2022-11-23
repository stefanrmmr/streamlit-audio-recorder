# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version April 2022

import os
import numpy as np
import streamlit as st
from io import BytesIO
import streamlit.components.v1 as components
import io
import soundfile as sf
from matplotlib import pyplot as plt
import keras
import tensorflow as tf
import predict
import preprocess
import librosa


# DESIGN implement changes to the standard streamlit UI/UX
st.set_page_config(page_title="streamlit_audio_recorder")
# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
    unsafe_allow_html=True)
# Design change st.Audio to fixed height of 45 pixels
st.markdown('''<style>.stAudio {height: 45px;}</style>''',
    unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
    unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
    unsafe_allow_html=True)  # lightmode


def audiorec_demo_app():

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # Custom REACT-based component for recording client audio in browser
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    # specify directory and initialize st_audiorec object functionality
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    # TITLE and Creator information
    st.title('RespiratorAI')
    st.write('\n\n')


    # STREAMLIT AUDIO RECORDER Instance
    val = st_audiorec()
    # web component returns arraybuffer from WAV-blob
    st.write('Audio data received in the Python backend will appear below this message ...')

    if isinstance(val, dict):  # retrieve audio data
        with st.spinner('retrieving audio-recording...'):
            ind, val = zip(*val['arr'].items())
            ind = np.array(ind, dtype=int)  # convert to np array
            val = np.array(val)             # convert to np array
            sorted_ints = val[ind]
            stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            wav_bytes = stream.read()

        # wav_bytes contains audio data in format to be further processed
        # display audio data as received on the Python side
        st.audio(wav_bytes, format='audio/wav')

        data_origin, samplerate = sf.read(io.BytesIO(wav_bytes))
        
        
        #take only first channel
        wav = data_origin[:,0]

        ### add resample to 4kHz here###
        data = librosa.resample(wav, samplerate, 4000)   

        fig, ax = plt.subplots()
        ax.plot(wav)
        ax.set_title(str(4000))
        st.pyplot(fig)

        #create preprocessor object
        preprocessor = preprocess.AudioPreprocessor()

        #load model
        model = keras.models.load_model('ResNet.h5', compile=False)

        #create predictor object
        predictor = predict.MyPredictor(model, preprocessor)

        #predict file
        y_pred = predictor.predict(wav)

        st.write(y_pred, samplerate)

if __name__ == '__main__':

    # call main function
    audiorec_demo_app()
