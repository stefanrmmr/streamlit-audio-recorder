# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version April 2022

import os
import streamlit as st
import streamlit.components.v1 as components

#
import logging
import queue
import threading

import matplotlib.pyplot as plt
import numpy as np
import pydub

from streamlit_webrtc import (
    RTCConfiguration,
    WebRtcMode,
    webrtc_streamer,
)
#

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


def run_guitar_tuner():
    """Transfer audio frames from the browser to the server and visualize them with matplotlib
    and `st.pyplot`."""
    webrtc_ctx = webrtc_streamer(
        key="guitar-tuner",
        mode=WebRtcMode.SENDONLY,
        audio_receiver_size=256,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"audio": True},
    )

    left_col, right_col = st.columns(2)
    left_col.json(GUITAR_TUNINGS)

    nearest_note = right_col.empty()
    off_metric = right_col.empty()
    fig_place = st.empty()

    fig, [ax_freq, ax_time] = plt.subplots(
        2, 1, gridspec_kw={"top": 1.5, "bottom": 0.2}
    )
    sound_window_len = 5000  # 5s
    sound_window_buffer = None
    while True:
        if webrtc_ctx.audio_receiver:
            try:
                audio_frames = webrtc_ctx.audio_receiver.get_frames(timeout=1)
            except queue.Empty:
                logger.warning("Queue is empty. Abort.")
                break

            sound_chunk = pydub.AudioSegment.empty()
            for audio_frame in audio_frames:
                sound = pydub.AudioSegment(
                    data=audio_frame.to_ndarray().tobytes(),
                    sample_width=audio_frame.format.bytes,
                    frame_rate=audio_frame.sample_rate,
                    channels=len(audio_frame.layout.channels),
                )
                sound_chunk += sound

            if len(sound_chunk) > 0:
                if sound_window_buffer is None:
                    sound_window_buffer = pydub.AudioSegment.silent(
                        duration=sound_window_len
                    )

                sound_window_buffer += sound_chunk
                if len(sound_window_buffer) > sound_window_len:
                    sound_window_buffer = sound_window_buffer[-sound_window_len:]

            if sound_window_buffer:
                # Ref: https://own-search-and-study.xyz/2017/10/27/python%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E9%9F%B3%E5%A3%B0%E3%83%87%E3%83%BC%E3%82%BF%E3%81%8B%E3%82%89%E3%82%B9%E3%83%9A%E3%82%AF%E3%83%88%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E4%BD%9C/  # noqa
                sound_window_buffer = sound_window_buffer.set_channels(
                    1
                )  # Stereo to mono
                sample = np.array(sound_window_buffer.get_array_of_samples())

                ax_time.cla()
                times = (np.arange(-len(sample), 0)) / sound_window_buffer.frame_rate
                ax_time.plot(times, sample)
                ax_time.set_xlabel("Time")
                ax_time.set_ylabel("Magnitude")

                spec = np.abs(np.fft.fft(sample))
                freq = np.fft.fftfreq(sample.shape[0], 1.0 / sound_chunk.frame_rate)
                freq = freq[: int(freq.shape[0] / 2)]
                spec = spec[: int(spec.shape[0] / 2)]
                spec[0] = spec[0] / 2

                peak = np.argmax(spec)
                peak_freq = freq[peak]

                note = get_nearest_note(peak_freq)
                real_freq = GUITAR_TUNINGS[note]
                off_metric.metric(f"Peak Frequency (Hz)", peak_freq, peak_freq - real_freq)
                nearest_note.header(note)


                ax_freq.cla()
                ax_freq.plot(freq, spec)
                ax_freq.set_xlabel("Frequency")
                ax_freq.set_yscale("log")
                ax_freq.set_ylabel("Magnitude")

                fig_place.pyplot(fig)
        else:
            logger.warning("AudioReciver is not set. Abort.")
            break



def audiorec_demo_app():

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # Custom REACT-based component for recording client audio in browser
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    # specify directory and initialize st_audiorec object functionality
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    # TITLE and Creator information
    st.title('streamlit audio recorder')
    st.markdown('Implemented by '
        '[Stefan Rummer](https://www.linkedin.com/in/stefanrmmr/) - '
        'view project source code on '
        '[GitHub](https://github.com/stefanrmmr/streamlit_audio_recorder)')
    st.write('\n\n')

    # STREAMLIT AUDIO RECORDER Instance
    st_audiorec()

    # use web-rtc
    run_guitar_tuner()


if __name__ == '__main__':

    # call main function
    audiorec_demo_app()
