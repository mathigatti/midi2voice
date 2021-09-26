import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="midi2voice",
    version="1.0.3",
    author="Mathias Gatti",
    author_email="mathigatti@gmail.com",
    description="Singing synthesis from MIDI file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mathigatti/midi2voice",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "music21", "Pyphen"],
    python_requires='>=3.6',
)
