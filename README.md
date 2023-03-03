# Jasper Chatbot
[![Documentation Status](https://readthedocs.org/projects/jasper-chat/badge/?version=latest)](https://jasper-chat.readthedocs.io/en/latest/?badge=latest)

A chatbot for my Twitch and Website that uses auto versioning via [Commitizen](https://commitizen-tools.github.io/commitizen/) and runs off [Rasa](https://www.rasa.com).

# Documentation
You can visit [ReadTheDocs](https://jasper-chat.readthedocs.io/en/latest/) online or you can follow the steps below to generate them locally, most more in depth information is documented here.

Most things below plus more in-depth information is located at the docs above which are also built from the `docs` dir.

## Building Docs Locally
You can cd into the `docs` dir and setup a python venv and install the `requirements.txt` file from this dir and then do `make html` to generate these, this is just using the typical sphinx setup nothing crazy.


# Environment Setup
I recommend if running on windows to setup WSL2 and setup ubuntu on it.  Then you can clone the repo to this setup and do `code .` with Visual Studio installed on your windows machine and edit the code,etc.  If you are on a Mac some of this will differ depending on Rasa.  Rasa up until recently had issues with silicon macs due to a tensorflow issue, this should have been resolved in the most recent version we are using.

First things you will need is ensure you have python 3.7 or higher installed, after having that you should be able to do the following to setup your virtual env:

`python3 -m venv .venv`

Now we can activate this virtual env and install our requirements.

Linux
`source .venv/bin/activate`

Windows
`.venv\Scripts\activate`

Once activated we can install with:
`pip install -r requirements.txt`

This will install [Rasa](https://www.rasa.com) and [Commitizen](https://commitizen-tools.github.io/commitizen/)

## Setting Up Action Server
For certain things to work that make external API calls you need to also run the action server, that can be done by using the same previous venv you already setup and activate it:

cd into the `actions` directory

`source .venv/bin/activate`

Then install the action server requirements:

`pip install -r actions.py`

There are also a few env vars/secrets used and we currently use [Doppler](https://doppler.com/join?invite=524473B9) for this but you can also just setup your own env vars via:

`export NASA_API_KEY=XXX` - This is the Nasa API where you can get your own key at https://api.nasa.gov/

`export GITHUB_TOKEN=XXX` - This is a GitHub API token that has access to read action builds and such, you can skip this if not building new intents or responses related to this.

For further information about not having to use these vars please see the docs at https://docs.doppler.com/docs/install-cli for more information and use https://doppler.com/join?invite=524473B9 to sign up for $100 free credit.

Now to run the action server you can do:

cd back to the main root of the repo `cd ..`

`rasa run actions`

If running with doppler would be:

`doppler run -- rasa run actions`

# How To Run Locally
After performing the above you can run the bot locally via:

`rasa run --cors '*' --debug`

# How To Deploy
This is deployed via the Rasa helm chart values file located in the `rasa` dir of [DevOps With Brian's LKE Repo](https://github.com/DevOps-With-Brian/devops-brian-lke/tree/main/rasa).

More info in that location can be found on deploying.