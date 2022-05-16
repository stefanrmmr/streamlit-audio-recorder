import pydub
import base64
import ffmpeg

import base64
from bokeh.io import curdoc
from bokeh.themes import Theme
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from pydub import AudioSegment

import streamlit as st

def rec_bokeh():

    audiofile_name = None

    rec_msg = '<p style="color: #e3fc03; font-size: 1rem;">After clicking this button you will <br>automatically be recorded for 15 seconds!</p>'
    st.markdown(rec_msg, unsafe_allow_html=True)
    stt_button  = Button(label="Start Recording", width=120, height=40, margin=(17, 0, 0, 17))

    stt_button.js_on_event("button_click", CustomJS(code="""
    const timeMilliSec = 15000 //Fixed 10sec recording
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        const mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();
        const audioChunks = [];
        mediaRecorder.addEventListener("dataavailable", event => {
          audioChunks.push(event.data);
        });
        mediaRecorder.addEventListener("stop", () => {
          //convert audioBuffer to wav
          const audioBlob = new Blob(audioChunks, {type:'audio/wav'});
          //create base64 reader
          var reader = new FileReader();
          reader.readAsDataURL(audioBlob);
          reader.onloadend = function() {
            //read base64
            var base64data = reader.result;
            //send data to streamlit
            document.dispatchEvent(new CustomEvent("GET_AUDIO_BASE64", {detail: base64data}));
          }
        });
        setTimeout(() => {
          mediaRecorder.stop();
        }, timeMilliSec);
      });
      """))

    result = streamlit_bokeh_events(
        stt_button,
        events="GET_AUDIO_BASE64",
        key="listen",
        refresh_on_update=False,
        override_height=75,
        debounce_time=0)

    if result:
        if "GET_AUDIO_BASE64" in result:
            b64_str_metadata = result.get("GET_AUDIO_BASE64")
            metadata_string = "data:audio/wav;base64,"
            if len(b64_str_metadata)>len(metadata_string):
                #get rid of metadata (data:audio/wav;base64,)

                if b64_str_metadata.startswith(metadata_string):
                    b64_str = b64_str_metadata[len(metadata_string):]
                else:
                    b64_str = b64_str_metadata

                decoded = base64.b64decode(b64_str)

                # st.write("Read sound from Frontend")
                st.write('Captured audio recording from web browser:')
                st.audio(decoded)

                #save it server side if needed
                uploaded_file = 'test.wav'
                with open(uploaded_file,'wb') as f:
                    f.write(decoded)

                #convert File to wav and save it again
                wav = AudioSegment.from_file(uploaded_file)
                getaudio = wav.export(uploaded_file, format="wav")

                # st.write("Read sound by saving in server and reloading file")
                # st.audio(uploaded_file)

                audiofile_name = uploaded_file

    return audiofile_name
