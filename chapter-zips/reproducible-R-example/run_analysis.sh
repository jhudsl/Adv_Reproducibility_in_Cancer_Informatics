#!/bin/bash

# C Savonen
#
# Download data from refine.bio and create a heatmap

set -e
set -o pipefail

# This script should always run as if it were being called from
# the directory it lives in.
script_directory="$(perl -e 'use File::Basename;
  use Cwd "abs_path";
  print dirname(abs_path(@ARGV[0]));' -- "$0")"
cd "$script_directory" || exit

# Run download script
python3 00-download-data.py

# Run heatmap Rmd
Rscript -e "rmarkdown::render('01-heatmap.Rmd', clean = TRUE)"
