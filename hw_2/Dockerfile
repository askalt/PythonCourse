FROM python:3.8

# Install latex requirements.
RUN apt-get update && apt-get install -y \
    texlive \
    texlive-latex-extra \
    texlive-fonts-recommended \
    && rm -rf /var/lib/apt/lists/*

# Install libraries.
ARG LATEX_VER=unknown
RUN pip install pdflatex
RUN pip install -i https://test.pypi.org/simple/ latex

# Copy image.
COPY ./artifacts/logo.png /artifacts/logo.png

# Copy source.
COPY main.py main.py
