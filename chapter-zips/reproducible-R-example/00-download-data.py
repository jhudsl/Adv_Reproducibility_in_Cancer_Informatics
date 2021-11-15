# C. Savonen 2021

# See refinebio-py tutorials for more info:
# https://alexslemonade.github.io/refinebio-py/quickstart.html

import os
from pathlib import Path
import pyrefinebio

# Define the file path to the data directory
data_dir = Path('data/SRP070849')

# Declare the file path to the gene expression matrix file
data_file = Path(os.path.join(data_dir, 'SRP070849.tsv'))

# Declare the file path to the metadata file
# inside the directory saved as `data_dir`
metadata_file = Path(os.path.join(data_dir, 'metadata_SRP070849.tsv'))

try:
  os.mkdir(data_dir, mode = 0o777)
except OSError as error:
  print(error)

# Only download the data if it doesn't exist locally
if not data_file.exists() or not metadata_file.exists():
    
    print("Downloading SRP070849 from refine.bio")

    pyrefinebio.create_token(agree_to_terms=True, save_token=False)

    pyrefinebio.download_dataset(
      "data/dataset.zip",
      "cansav09@gmail.com",
      experiments=["SRP070849"],
      extract=True
    )
