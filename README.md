
# Intro to Reproducibility in Cancer Informatics

[![Render Bookdown and Coursera](https://github.com/jhudsl/OTTR_Template/actions/workflows/render-bookdown.yml/badge.svg)](https://github.com/jhudsl/OTTR_Template/actions/workflows/render-bookdown.yml)

This course was created from [this GitHub template](https://github.com/jhudsl/OTTR_Template) and is the second part of the two part Reproducibility course. The first [part of the course is here](https://github.com/jhudsl/Reproducibility_in_Cancer_Informatics).

You can see the rendered course material here: https://jhudatascience.org/Adv_Reproducibility_in_Cancer_Informatics

If you would like to contribute to this course material, take a look at the [getting started GitHub wiki pages](https://github.com/jhudsl/OTTR_Template/wiki).

## About this course

This course introduces the concepts of reproducibility and replicability in the context of cancer informatics.
It is the first course in a two part course on reproducibility (the second part is not yet written but coming soon).
It uses hands-on exercises to demonstrate in practical terms how to increase the reproducibility of data analyses.
The course also introduces tools relevant to reproducibility including analysis notebooks, package management, git and GitHub.

## Learning Objectives

This course will teach learners to:  

- Become familiar with using GitHub in as a part of a analysis project workflow
- Engage in code review steps on GitHub.
- Pull and use an existing Docker image for running an analysis.
- Make data from a project clear and shareable.
- Write a simple Github Actions
- Obtain confidence to learn and apply additional reproducibility tools to an analysis.

## Encountering problems?

If you are encountering any problems with this course, please file a GitHub issue or contact us at {Some email or web address with a contact form}.

_All materials in this course are licensed [CC-BY](https://tldrlegal.com/license/creative-commons-attribution-(cc)) and can be repurposed freely with attribution._

## About the chapter example files

Each chapter has its own zip file to be downloaded as a learner is going through a particular chapter.

There are the Python and R versions.
For example, for chapter 2 there are:
```
python-examples/python-heatmap-adv-chapt-2
r-examples/r-heatmap-adv-chapt-2
```
These files are zipped up by a GitHub action so they are ready for easy downloading by the learner.
The user will download these according to the chapter and follow along with the chapter to make them more reproducible and eventually hopefully have something that looks like the "final" reproducible example versions.

This is the URL pattern they can find the chapter files at:

_For Python_:
```
https://github.com/jhudsl/Reproducibility_in_Cancer_Informatics/raw/main/chapter-zips/python-heatmap-chapt-4.zip
```
_For R_:
```
https://github.com/jhudsl/Reproducibility_in_Cancer_Informatics/raw/main/chapter-zips/r-heatmap-chapt-4.zip
```

## Obtaining the "final" versions of the example reproducible analyses

Both the "final" versions of the example analyses have their own repositories that are submodules of this one (located in their respective directories with the less reproducible versions of them in the `r-examples` and `python-examples` directories).
_Final_ here is in quotes because we may continue to make improvements to this notebook too -- this course tries to emphasize that work on data analyses should be iterative and we never have to say we're done with an analysis if we find other ways it can be improved!

- https://github.com/jhudsl/reproducible-python-example
- https://github.com/jhudsl/reproducible-r-example

## Running the R docker image:

With your current directory being the top of this repository, you can do:
```
cd r-examples/reproducible-r-example
docker build -f docker/Dockerfile . -t jhudsl/reproducible-r
docker run -it -v $PWD:/home/rstudio -e PASSWORD=password -p 8787:8787 jhudsl/reproducible-r
```
Then, in the browser of your choice, navigate to localhost:8787 ; using `rstudio` as your username and `password` as your password (or whatever you choose for your password in the command above). This docker image has the `renv` included in it.

### Running the Python docker image:

With your current directory being the top of this repository, you can do:
```
cd python-examples/reproducible-python-example
docker build -f docker/Dockerfile . -t jhudsl/reproducible-python
docker run --rm -v $(pwd):/home/jovyan/work -e JUPYTER_ENABLE_LAB=yes -p 8888:8888 jhudsl/reproducible-python
```
Then, in the browser of your choice, navigate to the port that the output tells you. This docker image will automatically have your conda environment set up and working.
