# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version April 2022

import os
import streamlit as st
import streamlit.components.v1 as components

# custom component for recording client audio in browser
parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
# specify directory and initialize st_audiorec object functionality
st_audiorec = components.declare_component("st_audiorec", path=build_dir)


def audiorec_demo_app():

    # DESIGN implement changes to the standard streamlit UI/UX
    st.set_page_config(page_title="streamlit_audio_recorder")
    # Design move app further up and remove top padding
    st.markdown('''<style>.css-1egvi7u {margin-top: -4rem;}</style>''',
        unsafe_allow_html=True)
    # Design change st.Audio to fixed height of 45 pixels
    st.markdown('''<style>.stAudio {height: 45px;}</style>''',
        unsafe_allow_html=True)

    # add title & creator information
    st.title('streamlit audio recorder')
    st.markdown('Mai 2022 - Implemented by '
        '[Stefan Rummer](https://www.linkedin.com/in/stefanrmmr/)')
    st.markdown('View project source code on '
        '[@GitHub](https://github.com/stefanrmmr/streamlit_audio_recorder)')


    # CREATE INSTANCE of "Streamlit Audio Recorder" - by stefanrmmr
    st_audiorec()


if __name__ == '__main__':

    # call main function
    audiorec_demo_app()
