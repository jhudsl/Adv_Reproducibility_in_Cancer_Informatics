FROM rocker/tidyverse:4.0.2
WORKDIR /rocker-build/

# Commonly used R packages
RUN Rscript -e  "install.packages( \
    c('BiocManager', \
      'R.utils', \
      'rprojroot'))"


RUN Rscript -e  "BiocManager::install( \
  c('BiocGenerics', \
    'BiocVersion'))"

# Set password default
ENV USER="rstudio" PASSWORD="rstudio" ROOT="TRUE"

CMD ["echo","Yay! I added to this Docker image"]
