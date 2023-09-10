from pathlib import Path
import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-audio-recorder",
    version="0.0.1",
    author="Stefan Rummer",
    author_email="stefan.rummer@outlook.com",
    description="[steamlit-audio-recorder by stefanrmmr] Streamlit Custom Component that enables recording audio from the client's mic in apps that are deployed to the web. (via browser Media-API, REACT-based)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stefanrmmr/streamlit-audio-recorder",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "streamlit>=0.63",
    ],
)