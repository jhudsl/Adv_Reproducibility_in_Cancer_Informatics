


# Using version control with GitHub

## Learning Objectives

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1013f9881e2_0_132.png){width=100%}

In the introductory part of this course, we discussed [some of the reasons for using GitHub](https://jhudatascience.org/Reproducibility_in_Cancer_Informatics/making-your-project-open-source-with-github.html#github-and-git-allow-you-to) but we didn't get into version control or GitHub's capabilities much beyond its capacity to store code in a place where others can find it.

In this advanced course, we will dig deeper into Git and GitHub's capabilities so you can really use this to your daily work's advantage. But, to gain the benefit of these deeper GitHub skills it will require some new habits to be formed. Fully embracing the GitHub workflow will make your work more efficient and help you create more transparent and reproducible analyses!

In this chapter we're going to introduce you one by one to the basic git commands you'll need as we do them!

## Prerequisites for this chapter

In order to complete this chapter **you will need a GitHub account (it's free)**. If you do not currently have a GitHub account, we recommend you go through our [Intro to Github chapter from the Introduction to Reproducibility course](https://jhudatascience.org/Reproducibility_in_Cancer_Informatics/making-your-project-open-source-with-github.html) first and then return to this chapter.

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g101867ebdaa_18_0.png){width=100%}

## Set up a Git Client (GitKraken)

Interaction with git and GitHub can be done completely from command line, but sometimes this can be harder to keep track of. So to help us navigate this, we recommend using a git client. There's a lot of different clients out there, and they are generally free for most situations you will need. In this course we will take you through how to use [GitKraken](https://www.gitkraken.com/git-client), one such git client.

GitKraken is nice because they have lots of nice tutorials, it works pretty well, and its free for most use cases. But if you find GitKraken doesn't work for you, you can explore [other git clients](https://www.hostinger.com/tutorials/best-git-gui-clients/). But for this course, we'll be using GitKraken.

### Install GitKraken

[Go here to install GitKraken](https://support.gitkraken.com/how-to-install/).

Follow their instructions to sign in with your GitHub account. It will ask you to authorize your GitHub account to connect to GitKraken. Click `Authorize`.

You may find it helpful to watch GitKraken's own tutorial (linked below) about how to "git" started, but we will also guide you through each step!


```
## PhantomJS not found. You can install it with webshot::install_phantomjs(). If it is installed, please make sure the phantomjs executable can be found via the PATH variable.
```

<iframe src="https://www.youtube.com/embed/ub9GfRziCtU" width="100%" height="400px"></iframe>

GitHub has a whole host of terms that can feel like a whole language at first, but we'll introduce them one at a time. To start, a lot of the GitHub workflow centers around handling copies of your code that are either stored on the internet (are _remote_) or are stored on your computer (are _local_).

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_120.png){width=100%}

A repository, in the case of a data science project, is mostly synonymous with the word "project". So using GitHub, a project will exist both as a remote repository and a local repository. (It will be on the internet on GitHub and on your computer).

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_149.png){width=100%}

## Get the exercise project files

In this course, you can work on the exercises from your own GitHub repository, but first we will need to set that up. Here we are providing you with the files you will want to upload to that repository.

Depending on whether you prefer to use R or Python, you can choose to follow this course using one or the other.

<details> <summary>**Get the Python project example files**</summary>
[Click this link to download](https://raw.githubusercontent.com/jhudsl/Reproducibility_in_Cancer_Informatics/main/chapter-zips/reproducible-python-example.zip).



Now double click your chapter zip file to unzip. For Windows you may have to [follow these instructions](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-f6dde0a7-0fec-8294-e1d3-703ed85e7ebc)).


</details>

<details> <summary>**Get the R project example files**</summary>
[Click this link to download](https://raw.githubusercontent.com/jhudsl/Reproducibility_in_Cancer_Informatics/main/chapter-zips/reproducible-R-example.zip).



Now double click your chapter zip file to unzip. For Windows you may have to [follow these instructions](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-f6dde0a7-0fec-8294-e1d3-703ed85e7ebc)).


</details>

## Start a GitHub repository

With the project files you've downloaded in the location you would like them to be, [open up your command line](https://towardsdatascience.com/a-quick-guide-to-using-command-line-terminal-96815b97b955#:~:text=Opening%20Command%20Line.&text=There%20are%20varying%20ways%20of,and%20press%20the%20return%20key.) and navigate to that being your current directory using the [`cd`](https://www.geeksforgeeks.org/cd-command-in-linux-with-examples/) and [`ls`](https://linuxize.com/post/how-to-list-files-in-linux-using-the-ls-command/) commands.

- Go to [Github's main page](https://github.com/) and click Sign Up if you don't have an account.
- Follow [these instructions to create a repository](https://docs.github.com/en/get-started/quickstart/create-a-repo). As a general, but not absolute rule, you will want to keep one GitHub repository for one analysis project.
  - Name the repository something that reminds you what its related to. For these examples, we're calling using `repository-name` as our placeholder.
  - Choose `Public`.
- Follow [these instructions](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository#adding-a-file-to-a-repository-on-github) to add all the files that are inside the `reproducible-R-example.zip` or `reproducible-python-example.zip` file you downloaded to this new repository.

This new repository you created should look [something like this](https://github.com/cansavvy/repository-name).

### git clone

Now you have a repository on GitHub online!


But in our daily grind, we will work on this code from our own computer. So to set this up, we'll need to `clone` it to our own computer. Cloning is just making a remote copy of the project local.

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_90.png){width=100%}

So to get started, you will need to clone the GitHub repository you created that we will be using for the duration of this course.

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_166.png){width=100%}

To clone a GitHub repository, using GitKraken. First, click `Clone a repo`. Then, choose where you’d like the repository to be on your computer using the `Browse` button. You will need to `Copy + Paste` your new repository's url to  where it says `URL`.

Navigate to your repository on GitHub to copy the URL. Copying and pasting is advisable because any little typo will inhibit cloning.

Now you are ready to click `Clone the repository`! It will ask you if you'd like to `Open Now`, click that.

### Create a branch

Handling branches is where you unleash the real benefit of GitHub, but it's also the confusing part to get a hang of.

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_266.png){width=100%}

The best way to get a grasp on what the branches represent is to create one and start using it.

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_632.png){width=100%}

In GitKraken we can create a new branch; this will be your working copy. First, click the Branch button. Next, type in a branch name in the box that the cursor is blinking in. In our example, we are calling it `a-new-branch`. Now click `Enter`! Now you have a new branch!

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_618.png){width=100%}

Now we can edit our files and code however we normally would. Go ahead and make an edit to any file in your new repository.

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_645.png){width=100%}

If you've made a change to any file in your repository, it will appear in GitKraken and you can click on it to see the differences.

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_652.png){width=100%}

If we want to add these file changes to our current branch, we need to `commit` them.

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_664.png){width=100%}

Now that we have changes committed to our branch we are ready to also add them to the remote, internet copy! To do this, we will need to `push` our branch.

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_686.png){width=100%}

To push means to add changes that are on your new branch to the remote branch (internet version). The word origin just refers to where your branch is stored on the internet. Choose your origin in the dropdown menu and click Submit.

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_786.png){width=100%}

After a variable number of commits, your branch, called a-new-branch is a different version of the original code base that may have a nifty improvement to it. But our main goal is to add that nifty improvement to the main branch. To start this process of bringing in new changes to the main curated repository, we will create a pull request.

From GitHub:

> Pull requests let you tell others about changes you've pushed to a GitHub repository. Once a pull request is sent, interested parties can review the set of changes, discuss potential modifications, and even push follow-up commits if necessary.

Pull Requests are the meat of how code changes and improvements get reviewed and incorporated! A vast majority of the benefits of incorporating GitHub into your workflow centers around fully utilizing the power of pull requests!

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_751.png){width=100%}

Now we can open up a pull request if we go to our GitHub repository on GitHub.

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_713.png){width=100%}

After you click on `Compare & pull request` you'll be taken to a screen where you can add information about your changes. After you are done writing your description, click `Create Pull Request`! (If you don't have your pull request description _perfect_ don't worry about it, you can always edit it later).

Congrats! You've just opened a pull request!

In an upcoming chapter we will discuss what information you should put in this pull request description to make it pertinent for yourself and whoever reviews your pull request.

To summarize, this is what this workflow looks like:

![](resources/images/03-version-control-with-github_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g1014c75158f_0_675.png){width=100%}

One more note, if you do want to use command line or you want to know more about the specific git commands that GitKraken is doing for you (might be handy for troubleshooting), **the specific commands that can be used or Googled at each step are highlighted in red in the images**, you just need to add `git` before them! So for example you would type `git push` in your command line in order to push your code. Or if you'd like to know more about pushing code, you can google `git push`.

## More resources for learning GitHub

- [Happy Git and GitHub for the useR](https://happygitwithr.com/) by @Bryan2021.
- [GitHub for data scientists](https://towardsdatascience.com/introduction-to-github-for-data-scientists-2cf8b9b25fba) by @Vickery2019.
- [Intro to GitHub](https://lab.github.com/githubtraining/introduction-to-github) by @GitHub2021.
- [First Day on GitHub](https://lab.github.com/githubtraining/first-day-on-github) by @GitHub2021c.
- [First Week on GitHub](https://lab.github.com/githubtraining/first-week-on-github) by @GitHub2021d.
- [GitHub docs about creating a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) by @GitHub2021b.
- [Making a Pull Request](https://www.atlassian.com/git/tutorials/making-a-pull-request) by @Radigan2021.
