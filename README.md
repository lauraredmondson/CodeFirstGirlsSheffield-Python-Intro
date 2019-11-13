# CodeFirstGirlsSheffield-Python-Intro
Course materials for the CodeFirstGirls Sheffield Introduction to Python Course

## Running the slides

### Method 1: Run via Python on your machine
To run the Jupyter Notebook slides, you need:
- [Python 3](https://www.python.org/downloads/)
- The `jupyter` Python package
- The `RISE` Python package

Install Python 3 with the link above. Then, open a terminal and run the following commands to install the `jupyter` and `RISE` package:
```bash
pip install jupyter RISE
```

If you also have Python 2 installed on your computer (i.e. if you are working on a Mac/Linux machine), you may have to replace `pip` with
`pip3` in the command above.

In the terminal, change to the directory containing the Jupyter Notebook slides, then run the following commands to start the Jupyter Notebook server
needed to run the slides:

```bash
jupyter notebook
```

### Method 2: Run with Docker
Alternatively, if your machine can run Docker (Windows 10 Pro, MacOS or any Linux distro), you can run the Jupyter Notebook server inside a Docker container.

To begin, [install Docker](https://docs.docker.com/install/) and the [Docker Compose](https://docs.docker.com/compose/install/) command line tool.
If you are on Windows or MacOS, Docker Compose will have already come with your Docker installation.

Then, at the root of the repository, type this single command to start the Jupyter Notebook server:

```bash
docker-compose up
```

You should see output similar to the following:

```bash
Starting jupyter-notebook ... done
Attaching to jupyter-notebook
jupyter-notebook | Executing the command: jupyter notebook
jupyter-notebook | [I 20:38:44.343 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
jupyter-notebook | [I 20:38:44.343 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
jupyter-notebook | [I 20:38:45.348 NotebookApp] Serving notebooks from local directory: /home/jovyan
jupyter-notebook | [I 20:38:45.348 NotebookApp] The Jupyter Notebook is running at:
jupyter-notebook | [I 20:38:45.349 NotebookApp] http://47e3a7c93868:8888/?token=c5abd1bcdfbb9f70d26eed5a045eb3a58dd7c1d9e8627b29
jupyter-notebook | [I 20:38:45.349 NotebookApp]  or http://127.0.0.1:8888/?token=c5abd1bcdfbb9f70d26eed5a045eb3a58dd7c1d9e8627b29
jupyter-notebook | [I 20:38:45.349 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
jupyter-notebook | [C 20:38:45.354 NotebookApp]
jupyter-notebook |
jupyter-notebook |     To access the notebook, open this file in a browser:
jupyter-notebook |         file:///home/jovyan/.local/share/jupyter/runtime/nbserver-6-open.html
jupyter-notebook |     Or copy and paste one of these URLs:
jupyter-notebook |         http://47e3a7c93868:8888/?token=c5abd1bcdfbb9f70d26eed5a045eb3a58dd7c1d9e8627b29
jupyter-notebook |      or http://127.0.0.1:8888/?token=c5abd1bcdfbb9f70d26eed5a045eb3a58dd7c1d9e8627b29
```

Unlike Method 1 which opens a browser automatically, you need to copy the URL beginning with `http://127.0.0.1:8888` in your browser instead
to see the same Jupyter user interface.
