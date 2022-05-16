# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version April 2022

import streamlit as st
import streamlit.components.v1 as components
import os 

# import design augmentation for streamlit UX/UI
import src.streamlit_design as streamlit_design

# custom component for recording client audio in browser
parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
# specify directory and initialize st_audiorec object functionality
st_audiorec = components.declare_component("st_audiorec", path=build_dir)


def audiorec_demo_app():

    # DESIGN implement changes to the standard streamlit UI/UX
    streamlit_design.design_setup()  # switch to primaryColor

    with st.expander("Streamlit Audio Recorder by stefanrmmr", expanded=True):

        st.title('streamlit audio recorder')
        st.markdown('Version 1.3.2 - April 2022 - '
            '[@GitHub](https://github.com/stefanrmmr/streamlit_audio_recorder)')

        st_audiorec()

if __name__ == '__main__':

    # call main function
    audiorec_demo_app()
