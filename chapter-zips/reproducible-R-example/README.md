# Reproducible analysis example - R

This is an example project repository to illustrate what a reproducible analysis might look like as discussed in more detail in the [Reproducibility in Cancer Informatics course](https://github.com/jhudsl/Reproducibility_in_Cancer_Informatics).  
It can be used as a template or otherwise borrowed from.

_This example analysis:_  

- Downloads [data from refine.bio](https://www.refine.bio/experiments/SRP070849/combination-targeted-therapy-to-disrupt-aberrant-oncogenic-signaling-and-reverse-epigenetic-dysfunction-in-idh2-and-tet2-mutant-acute-myeloid-leukemia-rna-seq) using the [refine.bio python API client](https://github.com/AlexsLemonade/refinebio-py).
- Identifies the top 90th percentile variant genes from the set.
- Creates and saves a heatmap from those genes.

It also has its own Docker image and GitHub actions to aid reproducibility.

## Requirements

To run this analysis you will need [`git`](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [`Docker`](https://docs.docker.com/get-docker/) installed on your computer.
These are two platforms that are very useful for reproducibility so they will be useful for you far beyond this repository.

## How to run the analysis

To re-run this analysis within its Docker image, open up your Terminal/Command Prompt.

1. First you can obtain a local copy of this repository by `git clone`-ing it.
```
git clone https://github.com/jhudsl/reproducible-r-example.git
```
2. Now navigate to the top of this repository.
```
cd reproducible-r-example
```
3. Use the following command to run the analysis:
```
docker run \
--mount type=bind,target=/home/rstudio,source=$PWD \
  jhudsl/reproducible-r \
  bash run_analysis.sh
```

## About the scripts

- `run_analysis.sh` - This main bash script runs the both steps of the analysis by calling the `00` and `01` scripts.

- `00-download-data.py` - This script uses the python client for the refine.bio API to download the processed and normalized data that is used to make a heatmap.

- `01-heatmap.Rmd` - This Rmd notebook takes the data that is downloaded by `00-download-data.py` and creates a heatmap that is saved to `plots/aml_heatmap.png`.

### Input

The [data used by this analysis](dataset can be downloaded from this page on refine.bio](https://www.refine.bio/experiments/SRP070849) is downloaded [processed and quantile normalized](http://docs.refine.bio/en/latest/main_text.html#refine-bio-processed-refinebio-processedibadge) from refine.bio using their API.
It is RNA-seq data from 19 acute myeloid leukemia (AML) mice models.

### Output

Two directories are created by this analysis and hold the output:  

`plots/` - contains the heatmap png: `aml_heatmap.png`
`results/` - contains the TSV file list of most variant genes: `top_90_var_genes.tsv`

## renv

Package management for this project is done with renv.
[If you don't have renv, you will need to install that first](https://rstudio.github.io/renv/articles/renv.html) with `install.packages("renv")`.

Follow the workflow describe by the renv introduction, but realizing that this repository already has an `renv` project initialized.
So in the `Console` window:

1. Use `renv::restore()` to load in the packages from the current `renv.lock` file.

> 2. Work in the project as normal, installing and removing new R packages as they are needed in the project,
> 3. Call renv::snapshot() to save the state of the project library to the lockfile (called renv.lock),
> 4. Continue working on your project, installing and updating R packages as needed.
> 5. Call renv::snapshot() again to save the state of your project library if your attempts to update R packages were successful, or call renv::restore() to revert to the previous state as encoded in the lockfile if your attempts to update packages introduced some new problems.

Be sure to add the `renv.lock` file to any commits and pull requests since that's what has stored the package changes to your environment!

## Docker

### Running the R docker image for development purposes

With your current directory being the top of this repository, run this command in your Terminal:
```
docker run -it -v $PWD:/home/rstudio -e PASSWORD=password -p 8787:8787 jhudsl/reproducible-r
```
Then in the browser of your choice, navigate to localhost:8787

### Rebuilding the docker image locally

If you prefer to build the image locally, or have otherwise modified the Dockerfile and want to test if it builds, you can run this command from the top of the repository:
```
docker build -f docker/Dockerfile . -t jhudsl/reproducible-r
```
Running `docker ps` should show you the `jhudsl/reproducible-r` listed with your images

## Github actions

There are two main GitHub actions in this repository:  

- `docker-management.yml` - Tests the building of the docker image upon changes to the `Dockerfile` being added to a pull request.
- `run-py-notebook.yml` - Re-runs the analysis by running `make_heatmap.ipynb` within the docker image (using the [command described above](#how-to-run-the-analysis)).

Both GitHub actions have the option [to be run manually](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow).
The Docker management GitHub actions also has the option to push the re-built Docker image to Dockerhub by setting `dockerhubpush` to `true`.
