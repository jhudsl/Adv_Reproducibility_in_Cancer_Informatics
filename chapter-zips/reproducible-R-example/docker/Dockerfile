FROM rocker/tidyverse:4.0.2
LABEL maintainer="cansav09@gmail.com"
WORKDIR /rocker-build/

# Install apt-getable packages to start
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils dialog

RUN apt-get -y --no-install-recommends install \
  python3-pip  python3-dev

RUN pip3 install \
  "pyrefinebio"

# Commonly used R packages
RUN Rscript -e  "install.packages( \
    c('renv', \
      'pheatmap'))"

# Set final workdir for commands
WORKDIR /home/rstudio
