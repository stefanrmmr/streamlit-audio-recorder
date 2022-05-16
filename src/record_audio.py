# FAIL: using pyaudio/portaudio does not work since it would try to access
# streamlits deployment server microphones and not the local browser window
# adding packages "libportaudio2" or "libasound-dev"  is no help in this issue

# FAIL: an approach using the sounddevice library has not been successful
# the code executes however the query for available sounddevices yiels no microphones

# FAIL: there is no opportunity to implement a html code including js elements
# using standard streamlit html components, button interaction/script not working

# METHOD: implementation of custom streamlit component with html css features
# and the opportunity to pass/receive data!
