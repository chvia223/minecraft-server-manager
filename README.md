# Overview
This is a discord bot that I made for personal use managing Minecraft servers for my friends. It takes advantage of the Google Cloud Platform(GCP) to automate a Linux VM to actually host the Minecraft servers. I used heroku to host the discord bot, but you can easily just run it on your own machine if you have Python installed. The only downside to this is the bot will not function if your computer is off. 

The discord bot will listen for user messages to perform start and stop actions for a specified Minecraft version that is available. I was able to make use of Google Cloud Functions, a feature of GCP, to target the VM boot and shutdown actions through HTTP Get requests.


I made this before I knew about Docker and Kubernetes, but now that I do know about them I think that I could make use of containerization to make this whole boot up/shutdown process more efficient and elegant. Those are the future plans for this project.

Accounts you will need:
* GCP account
* Discord account (and server)
* Heroku account (not necessary, but it's free and super useful)

I will make a tutorial/demo video soon to show all of the steps to set this up when I have time. In the mean time I'll link useful websites below.

[Software Tutorial/Demo Video](Not Working)

# Development Environment

* Git
* Github
* Python 3.8.5
* Google Cloud Platform Account
* Discord Account
* Discord Server
* Heroku Account

# Useful Websites

* [Google Cloud Platform Website](https://cloud.google.com)
* [Heroku Website](https://www.heroku.com/home)
* [Python Discord Bot Documentation](https://discordpy.readthedocs.io/en/stable/)
* [Python Discord Bot Tutorial](https://realpython.com/how-to-make-a-discord-bot-python/)
