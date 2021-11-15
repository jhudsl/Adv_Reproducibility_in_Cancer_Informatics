FROM jupyter/minimal-notebook
MAINTAINER cansav09@gmail.com

COPY environment.yml .

USER root

# Make sure this yml is permissions open for everybody.
RUN chmod 777 environment.yml

# Now make the environment
RUN conda env create -f environment.yml

# Pull the environment name out of the environment.yml
RUN echo "source activate reproducible-python" > ~/.bashrc
ENV PATH /opt/conda/envs/reproducible-python/bin:$PATH

# Install so we can find the correct kernel to run the notebook
RUN conda install nb_conda_kernels

SHELL ["conda","run","-n","reproducible-python","/bin/bash","-c"]
RUN python -m ipykernel install --name reproducible-python --display-name "Reproducible Python"
