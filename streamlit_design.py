# DESIGN CHOICES
import streamlit as st

def design_setup():

    # Design page layout and browser window details
    st.set_page_config(layout="centered",
                       page_icon="resources/rs_logo_transparent_yellow.png",
                       page_title="beat inspect")

    # Design move app further up and remove top padding
    st.markdown('''<style>.css-1egvi7u {margin-top: -8rem;}</style>''',
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

    # Design Audio Uploader Status Loading Bar Color
    st.markdown('''<style>.st-dp {background-color: #e3fc03;}</style>''',
        unsafe_allow_html=True)
    # Design Audio Uploader Status Loading Bar Color
    st.markdown('''<style>.st-dn {background-color: #e3fc03;}</style>''',
        unsafe_allow_html=True)


    # Design error message black colored texts
    st.markdown('''<style>.st-dm {color: black;}</style>''',
        unsafe_allow_html=True)


    # Design change spinner color to primary color
    st.markdown('''<style>.stSpinner > div > div {border-top-color: #e3fc03;}</style>''',
        unsafe_allow_html=True)

    # Design change hyperlink href link color
    st.markdown('''<style>.css-v37k9u a {color: #e3fc03;}</style>''',
        unsafe_allow_html=True)

    # Design change stMetricsValue to primary color via specific css-element
    st.markdown('''<style>.css-1xarl3l.e16fv1kl1 {color: #e3fc03;}</style>''',
        unsafe_allow_html=True)
    # Design change stMetricsValue top row subtitle to be slimmer
    st.markdown('''<style>.css-1gf0e5q {min-height: 0.5rem;}</style>''',
        unsafe_allow_html=True)

    # Design change st.Audio to fixed height of 45 pixels
    st.markdown('''<style>.stAudio {height: 45px;}</style>''',
        unsafe_allow_html=True)

    # Design change radio button inner point to be dark grey via custom css
    st.markdown('''<style>.st-d9 {background-color: black;}</style>''',
        unsafe_allow_html=True)
    st.markdown('''<style>.st-da {height: 8px; width: 8px;}</style>''',
        unsafe_allow_html=True)

    # Design change radio button padding for horizontal alignment
    st.markdown('''<style>.st-de {padding-left: 8px; padding-right: 8px;}</style>''',
        unsafe_allow_html=True)
    # Design change radio button title div size to zero height
    st.markdown('''<style>.css-16huue1 {min-height: 0rem;}</style>''',
        unsafe_allow_html=True)
    st.markdown('<style>div.row-widget.stRadio {margin-top: -2.5rem;} </style>',
             unsafe_allow_html=True)

def radiobutton_horizontal():
    # Design change radio button layout to be horizontally aligned
    st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>',
             unsafe_allow_html=True)
