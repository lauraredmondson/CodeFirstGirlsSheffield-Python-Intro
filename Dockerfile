FROM jupyter/minimal-notebook:latest

RUN pip install RISE

# build command: docker build -t jupyter-with-rise:latest ./
