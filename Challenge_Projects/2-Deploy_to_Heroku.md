# Challenge Project: Deploy to Heroku

## Description

Suppose you want to deploy your finished baby name popularity tracker to the web so it can be publicly accessible. You have a few options:

- You could buy your own computer to use as a server, set it up to run your application and serve pages, connect it to the Internet, and configure a domain name to point to it.
- 
- You could **rent** infrastructure from a cloud provider, like Amazon Web Services (AWS). These services allow you to deploy apps that run on **another company's** infrastructure so you don't have to undertake the overhead of mainintaing and configuring your own hardware.  A large number of companies, particularly early stage startups, use AWS or other cloud providers for all of their server needs. There is still, however, nontrivial complexity involved in getting cloud infrastructure up and running.

Most tech companies have a dedicated "Development Operations" (**DevOps**) staff that has the responsibility of managing the company's testing and deployment infrastructure, whether those resources are located in the company's own datacenter or rented from a cloud provider.

Heroku is a "platform as a service" (PaaS) that provides a simplified interface to deploy applications to Amazon EC2. Briefly, as a developer, you can write your code and then push it to Heroku's servers, which handle all of the back-end work to deploy your app on Amazon's cloud platform and make it publicly accessible. **This is very cool**. Heroku's value proposition is to free software developers to focus on creating code that solves problems and achieves business goals, rather than managing the infrastructure required to deploy and run their apps.

In this project, you're going to take your baby names app and deploy it to Heroku. This doesn't require any additional coding, but will allow you to get additional practice with the command line and git. At the end, you'll have a working web app tied to a URL that you can share with anyone interested in your work.

## Submission

Complete the steps below to deploy your app. At the end of the process you should have a complete version of the application running on a Heroku URL. Send me the URL and answers to the questions below on Slack. I'll check everything out and give you credit for this project. Successfully completing this project will raise your final grade by **one part of a letter** (e.g., from B to B+ or B+ to A-).

## Setup

First, sign up for a Heroku account. This is **free** for personal development projects &ndash; Heroku allows a basic account to run apps for about 1000 hours per month and pauses your apps once they go idle for 30 minutes.

The first major step is to install Heroku's tools. Within Mimir, download and install the Heroku command-line interface (CLI). The command below pulls the CLI from Heroku's servers and installs it to your local Mimir session. The local session is cleared when your Mimir workspace shuts down, so you'll need to re-run this command to reinstall the CLI if you want to use it later.

```
curl https://cli-assets.heroku.com/install.sh | sh
```

Log in to Heroku from the command line and enter your credentials:

```
heroku login -i
```

## Version Control and Git

There are multiple ways to deploy a Heroku application. We're going to take advantage of Heroku's support for Git, the most popular **version control system** that developers can use to keep track of their code.

Before proceeding, read the following articles.

- https://www.atlassian.com/git/tutorials/what-is-version-control
- https://guides.github.com/introduction/git-handbook/ (The first three sections, up to and including "Basic Git Commands." You don't have to memorize the commands.)

Now answer these questions about Git and version control systems.

- What are three primary benefits of version control systems in general?
- Name at least two other version control sytsems besides Git.
- What does it mean to say that Git is a "distributed version control system?" How is that different from a non-distributed system?
- What is a Git repository?
- Give general definitions of the terms "commit" and "merge" as they apply to Git.

## Deploy

### Git repos

You can now `cd` into your project directory.

```
cd CMS_120/Flask
```

The first that you need to do is make your project repo into a Git repository.

```
git init
```

This command will create a special `.git` repository inside `Flask`. Names starting with `.` are considered "hidden" by the shell, which means they don't show up in the output of a regular `ls` command. To view "hidden" files and folders use

```
ls -a
```

**Question**: Do some research to discover the purpose of the `.git` folder. What does it contain, in general terms?

### Setup the project for Heroku

Heroku is pretty slick and will automatically build and deploy your application on the Internet. However, it needs two additional pieces of information to build Python projects.

- A file named `Procfile` that informs Heroku of the name of your application. In our case, this is `app.py`.
- A file called `requirements.txt` that specifies which versions of the required packages to load. This file exists to ensure that Heroku can create your app with the correct versions of all the dependencies it needs and not accidentally break something by loading the wrong version.

Create a file named `Procfile` in your `Flask` directory (just `Procfile`, no extension). Put the following line in it:

```
web: gunicorn app:app
```

The line tells Heroku to use a web server program called `gunicorn` (which is short for "Green Unicorn" and not, like, a unicorn with a gun for a horn) to run `app.py`.

Next, create `requirements.txt` and give it the following lines:

```
click==7.1.2
Flask==1.1.2
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
numpy==1.19.5
pandas==1.1.5
python-dateutil==2.8.1
pytz==2021.1
six==1.15.0
Werkzeug==1.0.1
```

Each line defines a package that's used by the Flask framework, plus `pandas`, `numpy` and a few other packages that the program requires. Make sure you have both files saved in the `Flask` directory.


### Heroku project

We are now ready to push the application to Heroku. Create a new Heroku project.

```
heroku create
```

This command will assign you a new project URL on Heroku's domain. It will also create a connection to a remote Git repository stored on Heroku's servers that you will use as the deployment point for your code in a moment.

### Commit and push

Git, like all version control systems, exists to track changes to projects. However, **Git does not automatically track every change you make to a file in the repo**. Instead, you must manually **commit** your changes to make Git record them. Recall that you created a new empty Git repo with `git init` in an earlier step. You must now commit all of your files to the repository.

To commit, you must first **stage** the new and updated files. Use the following command to stage all changes made within the repo:

```
git add .
```

You can view the list of staged changes with 

```
git status
```

Use the `commit` command to commit the changes to the local repository. The `-m` flag specifies a message describing the nature and purpose of the commit and is required.

```
git commit -m "Search engine app"
```

You will see some output showing that Git has incorporated your changes into the local repository, modifying some files and creating others.

To deploy, **push** the contents of your Git repo on Mimir to the remote Git repo on Heroku. When you do this, Heroku's machinery will kick in to build the project and automatically deploy it to the web:

```
git push heroku master
```

You should see a ot of output indicating that Heroku is building the project. This will **probably** work. If it does fail, look carefully at the output for an explanation of why the build failed. The most likely reason for a failure is a package in `requirements.txt` listed with a version that Heroku can't support. If that does happen, Heroku will print out a list of acceptable versions for the problematic package. Update `requirements.txt` to use a version of the package that Heroku supports, then repeat the `git` commands to `add`, `commit`, and `push` your work.

When you're done, you can go to the URL give to your be Heroku create and see your project!

### Making further changes

You may want to continue making updates to the application. This is easy.

- You **don't** need to create a new Heroku project. Keep using the same project.
- Make and test your changes on Mimir, just as you did when originally building the app.
- When you have the app working the way you want, repeat the Git commands given above to add, commit, and push the project changes.
- There's no limit to how many times you can update the app, but Heroku will only build and deploy one new version at a time.
