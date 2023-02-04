# chatbot-auto-versioning
Setting up auto versioning using [Commitizen](https://commitizen-tools.github.io/commitizen/) on a basic [Rasa](https://www.rasa.com) chatbot.

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

# How To Run Locally
After performing the above you can run the bot locally via:

`rasa run --cors '*' --debug`

