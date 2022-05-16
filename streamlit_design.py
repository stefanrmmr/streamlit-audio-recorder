# DESIGN CHOICES
import streamlit as st

def design_setup():

    # Design page layout and browser window details
    st.set_page_config(layout="centered",
                       page_title="streamlit_audio_recorder")

    # Design move app further up and remove top padding
    st.markdown('''<style>.css-1egvi7u {margin-top: -9rem;}</style>''',
        unsafe_allow_html=True)

    # Design hide top header line
    hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    # Design hide "made with streamlit" footer menu area
    hide_streamlit_footer = """<style>
                            #MainMenu {visibility: hidden;}
                            footer {visibility: hidden;}
                            </style>"""
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)

    # Design change hyperlink href link color
    st.markdown('''<style>.css-v37k9u a {color: #e3fc03;}</style>''',
        unsafe_allow_html=True)

    # Design change st.Audio to fixed height of 45 pixels
    st.markdown('''<style>.stAudio {height: 45px;}</style>''',
        unsafe_allow_html=True)
