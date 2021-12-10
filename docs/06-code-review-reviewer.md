


# Engaging in Code Review - as a reviewer

## Learning Objectives

![](resources/images/06-code-review-reviewer_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfc3e8b194d_0_236.png){width=100%}

## Reviewer responsibilities in code review

When reviewing a pull request, you take on responsibility to ensure that the pull request is getting the project to a better state than before.

There are three aspects to reviewing we will focus on:  

1. Identify areas in the code and documentation that are opportunities for improvement.
2. Communicate your questions and concerns effectively and in a way that creates a positive atmosphere.
3. Determine solutions collaboratively in a way that allows for a learning as well as a long term improved product.

### What to look for!

Depending on the goals of the project, and pull request there can be a lot to keep an eye out for. There are [many articles out there about what to look for in a code review](https://github.com/joho/awesome-code-review#articles).

_Here's some general points:_  

- Does the analysis answer the question it's asking? Are the methods it uses to do so appropriate?
- Is the code clear and readable? Does it contain a healthy amount of comments and documentation for individuals not familiar with the project to understand generally what is going on?
- Is the code efficient with computational resources? (Are there areas it's a bit too greedy with memory usage?)
- Does the code stick to the style and conventions of this project?
- Are there alternate scenarios where the current strategy might fail? (depending on the likelihood of this use case, this may be an instance for a new issue and for it to be addressed in a different pull request).

### How to communicate it

The pull request may be the author’s precious bundle. Try to be empathetic to the learning process! You are both working on this project together -- assume you both want the best out of this project. If something seems wrong, work together to find a solution, don't ever waste time on placing blame.

![](resources/images/06-code-review-reviewer_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g102298f211a_0_20.png){width=100%}

Remember that everything sounds harsher when you don't have in-person cues! In this example, Avi may be stating factual things, but without his pleasant and reassuring disposition, it can feel super harsh.

![](resources/images/06-code-review-reviewer_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfc3e8b194d_0_177.png){width=100%}

If Avi had reframed his comments, they might be more effective in this collaboration. @Babatunde2018 suggests framing [review comments in three ways to help communication: questions, suggestions, and appreciations](https://medium.com/@otarutunde/comments-during-code-reviews-2cb7791e1ac7).

#### Questions

_For example:_  

> What happens if this doesn’t get saved? Does it throw an exception or fails silently?

The key is to be specific with the questions. Mention exact file names. Put comments on the line you are referring to. Explain what you think is happening and ask them to explain if that is correct.  

#### Suggestions

_For example:_  

> I suggest you use an ArrayHelper getValue method here because of its error handling capability instead of accessing the value directly
You could even go further by giving an example:
$a = $b[‘key’]; would raise an error if key is not set but $a = ArrayHelper::getValue($b, ‘key’); would return a null value if key is not set.

Giving suggestions and explain not only how to implement it but why it might be preferred in this scenario is a great learning process both for the author and yourself.

#### Appreciations

Start every review comment with an appreciation for the hard work completed! This goes a long way for creating a positive atmosphere.

_For example:_  

> Nice Job! Alice. I suggest we create an interface for this service so other substitute services can implement the interface as well, this would enable us change to a different service with very minimal efforts when the need arises. What do you think?

Let's see how Avi's message could have been reworked to give a more effective review:  

![](resources/images/06-code-review-reviewer_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_gfa97af8537_0_55.png){width=100%}

This interaction reminds us that effective code review is steeped in empathy from both sides. Authors need to appreciate the time and effort the reviewer is spending to help them; while reviewers need to be sensitive to the amount of effort put in by the author already.

![](resources/images/06-code-review-reviewer_files/figure-docx//1IJ_uFxJud7OdIAr6p8ZOzvYs-SGDqa7g4cUHtUld03I_g102298f211a_0_35.png){width=100%}

### Exercise: Review Past you's code

1. Find the oldest code you wrote and currently have on your computer.
2. Create a repository and pull request with this old code, following the general steps for creating a repository and pull request [from the previous chapter](https://jhudatascience.org/Adv_Reproducibility_in_Cancer_Informatics/using-version-control-with-github.html#start-a-github-repository).
3. Request yourself as a reviewer.
4. Review the code on Github using [their docs as a guide for the mechanics of it](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request).
5. As you review, have empathy for past yourself, and give questions, appreciations, and suggestions in regards to this code.

#### Recommended reading about code review

- [Comments during Code Reviews](https://medium.com/@otarutunde/comments-during-code-reviews-2cb7791e1ac7) by @Babatunde2018
- [On Empathy and Pull Requests](https://slack.engineering/on-empathy-pull-requests/) by @Hirpa2016.
- [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) by @Hauer2018.
- [Your Code Sucks! – Code Review Best Practices](https://quickbirdstudios.com/blog/code-review-best-practices-guidelines/) by @Hildebr2020.
- An even longer list of [readings about code review](https://github.com/joho/awesome-code-review)

**If you have any feedback on this chapter, please [fill out this form](https://forms.gle/j3cJZX5CmNtQp6QKA), we'd love to hear your feedback!**
