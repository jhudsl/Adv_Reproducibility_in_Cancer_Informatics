


# Launching a Docker image

## Learning Objectives

![](resources/images/07-launching-docker_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfa97af8537_0_81.png){width=100%}

***

In the introductory part of this course, we discussed [package managers](https://jhudatascience.org/Reproducibility_in_Cancer_Informatics/managing-package-versions.html) like renv or conda. Recall that even if you have the same packages installed between two computers, you can still get different results!

![](resources/images/07-launching-docker_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfd7f4e514e_0_256.png){width=100%}

This is because package versions _do_ influence results as demonstrated by @BeaulieuJones2017.
Package managers address part of this problem, however their limitation is that generally only can help with certain sets of packages. `conda` really only manages `conda` installed packages and `renv` doesn't help with package management outside of R. Both of these have limited capabilities for cross platform shipping.

This is where Docker can help fill in the gaps.

> I don’t even count anymore how many times did my code break when someone else run it. The strange part was — it worked on my machine. That’s where Docker saves the day. If it works on your machine, it will work on any.

@Radecic2020

![](resources/images/07-launching-docker_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfd7f4e514e_0_0.png){width=100%}

## What's Docker?

One way to ensure that her collaborators have the same computing environment is Ruby could ship her computer to each of her collaborators and have them run the analysis on her computer. But before you buy hundreds of laptops for your projects, we'll show you how Docker will allow you to send your computing environment to your collaborators in a practical manner.

![](resources/images/07-launching-docker_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfd7f4e514e_0_5.png){width=100%}

Ruby can create a Docker image that Avi can use to run the analysis. This way Ruby and Avi know they are using the same computing environment. Now if Ruby and Avi obtain different results, it won't be because of version differences.

![](resources/images/07-launching-docker_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfd7f4e514e_0_55.png){width=100%}

## Install Docker

Go here to [install Docker](https://www.docker.com/get-started), following the instructions for your particular operating system.

If you don't have a Docker account create an account when prompted, or [go here](https://hub.docker.com/).
After you install Docker, start up Docker desktop by double clicking on the app. It may take some time to start up.

## Getting started with Docker

1. Open up your [command line](https://towardsdatascience.com/a-quick-guide-to-using-command-line-terminal-96815b97b955).
2. First we need to get the Docker **image**. A Docker image is like a snapshot of your computing environment that you can move from place to place. We can download images from online and then use them to make a container. Containers are what we use to actually run analyses.

![](resources/images/07-launching-docker_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfbb8cb91d5_0_116.png){width=100%}

From command line, run one of these commands depending on whether you'd like to use Python or R:

<details> <summary> To obtain the **python docker image** </summary>
```
docker pull jhudsl/reproducible-python
```
</details>

<details> <summary> To obtain the **R docker image** </summary>
```
docker pull jhudsl/reproducible-r
```
</details>


3. Open up the Docker Desktop app. Click on 'images' on the left. This shows the images you currently have available on your computer.


![](resources/images/07-launching-docker_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfbb8cb91d5_0_237.png){width=100%}

4. Return to your command line. Using [`cd`](https://www.geeksforgeeks.org/cd-command-in-linux-with-examples/) and [`ls`](https://linuxize.com/post/how-to-list-files-in-linux-using-the-ls-command/) navigate to your project repository (or whatever files you'd like to be accessible in your development environment) and we can start up a docker container using `docker run`.


<details> <summary> To run the **Python docker image** </summary>
```
docker run --rm -v $PWD:/home/jovyan/work -e JUPYTER_ENABLE_LAB=yes -p 8787:8787 jhudsl/reproducible-python
```
Now in your internet browser, go to the address printed out. It should take you to Jupyter Lab.
Now you are ready to develop inside a Docker container!

</details>

<details> <summary> To run the **R docker image** </summary>
But you can change the `password` to whatever you'd like.
```
docker run --rm -v $PWD:/home/rstudio -e PASSWORD=password -p 8787:8787 jhudsl/reproducible-r
```
Now in your internet browser, go to `localhost:8787`. You should see an RStudio login page.

Login to RStudio. Your username will be `rstudio` and your password, will be whatever you set your password to be.

Now you are ready to develop inside a Docker container!

</details>

To see what containers you have running or to clear out old containers, in Docker Desktop you can go to the `Containers/Apps` page.

![](resources/images/07-launching-docker_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfc8849fa4d_0_10.png){width=100%}

### A Breakdown what these Docker run options are

[Docker has super extensive documentation](https://docs.docker.com/)! But to get you started, here's the highlights for this `docker run` command:

![](resources/images/07-launching-docker_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfbc11e6ab0_0_18.png){width=100%}

- **The remove option (`--rm`)**	Automatically removes the container when docker run exits.
- **The volume option (`-v`)** is how you specify what files you’d like available in the container and where to find them. In this instance we are using the output of the pwd command (print working directory) so that wherever you run this command, the files in that directory will be available in the container. The part after the colon specifies where these files will be found in the container.
- **The environment option (`-e`)** is how you can specify any environment variables you will need. In this instance for the rocker image we need to specify a password. but for the python image we needed to specify `JUPYTER_ENABLE_LAB=yes` so that we can use Jupyter Lab.  
- **The port option (`-p`)** is how you specify what port you can connect to this on using your internet browser.
- **The image** to use is specified in the last part of the `docker run` command says what image to run, so in these instances, we are running a container using the `jhudsl/reproducible-r` or `jhudsl/reproducible-python` images.

## More about Docker

- [Docker tutorial for beginners](https://docker-curriculum.com/) by @Srivastav2018.

#### Python specific:

- [Jupyter Docker stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) by @ProjectJupyter2018.
- [How to Run Jupyter Notebook on Docker](https://towardsdatascience.com/how-to-run-jupyter-notebook-on-docker-7c9748ed209f) by @Okada2021.

#### R specific:

- [Launching RStudio in Docker](https://jsta.github.io/r-docker-tutorial/02-Launching-Docker.html) by @openscilabs2021.
- [Getting started with R and Docker](https://mdneuzerling.com/post/user-getting-started-with-r-and-docker/) by @Neuzerling2018.

**If you have any feedback on this chapter, please [fill out this form](https://forms.gle/j3cJZX5CmNtQp6QKA), we'd love to hear your feedback!**
