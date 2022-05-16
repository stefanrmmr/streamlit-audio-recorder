# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version April 2022

import os
import streamlit as st
import streamlit.components.v1 as components

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
    # LIGHTMODE custom component for recording client audio in browser
    # (alternatively there is also source code provided for darkmode design)
    build_dir_light = os.path.join(parent_dir, "st_audiorec_light/frontend/build")
    # specify directory and initialize st_audiorec object functionality
    st_audiorec_light = components.declare_component("st_audiorec", path=build_dir_light)

    # TITLE and Creator information
    st.title('streamlit audio recorder')
    st.markdown('Implemented by '
        '[Stefan Rummer](https://www.linkedin.com/in/stefanrmmr/) - '
        'view project source code on '
        '[@GitHub](https://github.com/stefanrmmr/streamlit_audio_recorder)')
    st.write('\n\n')

    # COLUMNS for custom alignment
    audio_col0_, audio_col1_ = st.columns([1, 0.5])
    with audio_col0_:
        # STREAMLIT AUDIO RECORDER Instance
        st_audiorec_light()


if __name__ == '__main__':

    # call main function
    audiorec_demo_app()
