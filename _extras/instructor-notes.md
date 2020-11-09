---
layout: page
---
## Setup
I recommend using a portrait layout for screen sharing so that students have space on their screen to open their own shell/Stata. We will encourage dual screens, but not all will be able to do it. In Zoom, click on "Share screen," "Advanced," and "Portion of screen." This way you can select a fixed rectangle on your screen to share. Make sure to move applications around your screen *before* you begin the class.

Use dark font on white background and at least 18p-sized font. Set this in advance for both Bash and for Stata.

Zoom host can make others host or co-host. Even if host's network breaks down, meeting stays online. There are polling buttons under "Participants", which can be used to substitute for green and red stickies. Zoom aggregates poll results there, that is, you can see how many participants have voted "Yes" vs "No."

## Shell
Before the lesson, unzip the [data file](https://zenodo.org/record/3994932/files/dc-economics-v2.1.zip?download=1) in the Downloads folder in your home directory.

The key objective of this lesson is to make learners comfortable navigating the folders on their computer and accessing files from *different* folders using relative paths. It is also important that they can look into .csv files without messing them up in Excel or other spreadsheet editor. 

To discourage the usage of Excel, you can refer to the current case of having to rename lots of genes because their names are read as dates in Excel, leading to many errors in genetics publications.

Before starting the lesson, make sure to remind learners to unzip the folder. In windows it might look like it's a normal folder (rather than zipped).

Remind that `man` command does not work in Git-Bash. You should type `<command> -- help ` instead.

### Topics and commands to cover

`pwd`, `ls`, `cd`, `mkdir`, `head`, `cp`

1. Navigating directories with `pwd`, `cd` and `ls` (Episode 2)
2. How to look into a .csv file with `head` (skip wildcards from Episode 3)
3. Creating directories and copying files (stop short of permissions)


## Git
We are using command line git to reinforce the concepts. At the end, you may show a GUI client to learners, but not before, so as not to confuse them.

Before the lesson starts, it is useful to give a conceptual introduction to git, referring learners to tools they already know, like undo, creating copies manually and Dropbox. For example,

> ### Git vs Dropbox
> We are all familiar with the problem of saving different versions of our files to make sure that we can go back when necessary. How many of you have created copies with different file names like "manuscript_revision2_final7.tex"? (Wait for reactions.) How many has a system for this like a filename based on dates, version numbers or author initials? (Wait for reactions, likely much fewer.) How many are using Dropbox, Google Drive or a similar tool to share files with coauthors?
> 
> A version control system like git handles all these issues. We can save each version of a project, share it with coauthors, who will know when the version was created, who saved it and will also see a short message about what that version is about.
>
> A key difference to Dropbox, which shares our files automatically, is that we will have to explicitly declare that we want to save a new version. This is a bit more work, but is worth it, because our coauthors will understand better who change what when.
{: .discussion}

The lesson is following a GitHub-based workflow. Make sure everyone has a GitHub account *before* starting this lesson.

We are skipping Episode 5, "Labeling Things." In practice, it is quite rare that we need to check out an old commit. We are only teaching students how to make this possible with using proper version control.

Pushing and pulling (Episode 6) are importants parts of the GitHub-based workflow. If you finish early, Episode 10 about sharing repositories with others could be a good next step. 

> ### Beware of GitHub's responsive UI
> GitHub's website has a responsive layout, which is helpful if you read it on a mobile device, but can be confusing if learners see something different than what is on your screen. Spend a minuted at the beginning to familiarize yourself and learners with the layout, the location of key links and buttons.
{: .callout}

## Data Wrangling with Stata
We are using Stata 16, but some learners may have earlier versions, so the lesson does not yet include data frames. Also note that some learners may not have tab completion yet.

The current working directory is am important concept to solidify in Stata, too, so make sure your screen share included this bottom line of the Stata window.

Proper Stata style is important, so write out commands in full (yes, even when live coding) and use relative paths with full filename extensions. We want learners feel like they are coding, not poking around in an app.

We seem to spend an inordinate amount of time on import delimited options. This is because reading data from "standard" formats is an important part of the workflow if you are to think of Stata as a tool in your tool chain, not as an interactive application. 

## Coding with Stata
The key mental model to share with learners: Stata is a tool that you can use most effectively like an interpreted programming language. In particular,

1. Save every data manipulation step in a .do file
2. Use .do files as scripts creating (preferably one) output from inputs
3. So much so that these scripts may even be called from the command line (optional, if time permits)

Getting this mental model across is the most important, everything else, like particular commands, are secondary. 

## Roles
### Instructors
Instructors share their screen while live coding. They can also take audio questions.

### Co-instructors
Co-instructors are running the show in each room. They are watching questions, learner status and *keeping track of time*. They amplify questions to the instructor if necessary.

They also copy polls [from the document](https://docs.google.com/document/d/1q0iYEjvCnDmj8D-PlOpGHg214Sfq8HO4aS7bwTYJhS4/edit?usp=sharing) to the Slack channel of their room whenever it is appropriate.

### Helpers
Learners will ask for help in the topical Slack channels. Zoom audio and hand signals may also signal that a learner is stuck, but discourage the use of Zoom chat so that all written discussion is in the same place for everyone to learn from.

If you find it helpful, ask the learner to share a screenshot of their problem.

When answering to a learner question on Slack, use "*Reply in thread*" so that the discussion is available for other to check but does not pollute their Slack channel.
