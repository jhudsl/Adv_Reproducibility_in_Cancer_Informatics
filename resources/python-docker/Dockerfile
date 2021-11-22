FROM jupyter/minimal-notebook

USER root

# Upgrade pip
RUN conda update pip

# Install pip packages
RUN pip3 install \
  numpy==1.20.3 \
  pandas==1.3.3

CMD ["echo","Yay! I added to this Docker image"]
