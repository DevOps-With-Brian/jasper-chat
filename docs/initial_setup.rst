**************
Initial Setup
**************
This section covers how to initially setup Jasper locally and test the bot and interact with it.


Pre-Req's
-----------
This requires a few things to work.  You need to have `Python3 <https://www.python.org/downloads/>`_ installed first off.  At the time of writing this, it has been tested with 3.8.10.  It should work with newer versions per Rasa's requirement.  Please ensure you have python before continuing.

Secrets & Env Vars
-------------------
There are a few secrets/env vars used for this to work correctly.  They are listed below as well as a section about Doppler which is a SecretOps platform that would allow for easier management of them.

:literal:`NASA_API_KEY` - This is the `Nasa API <https://api.nasa.gov/>`_ where you can get your own key

:literal:`GITHUB_TOKEN` - This is a GitHub API token, You will need to set this up if you want the checks against your repos/public repos, `How-to Create Fine Grained Access Token <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-fine-grained-personal-access-token>`_

Typically you would need to export these via a .env file or exporting on the cmd line before running anything, however you can look at the next section about Doppler to see a easier way, it is not required to use this project.

Doppler SecretOps Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Doppler is a SecretOps platform that allows you to maintain env vars and secrets throughout the development lifecycle.  So you can use env vars from dev locally and then have updated ones in prod that are used say from a kubernetes operator.

To sign up and for more general information please go `Here <https://doppler.com/join?invite=524473B9>`_ you will also recieve $100 in free credit if you decide to upgrade outside of the free tier.

For documentation on what we are referencing below you can look at `Dopper CLI Docs <https://docs.doppler.com/docs/install-cli>`_

The basic workflow if using doppler would be setup your env vars in dev and then run:

.. parsed-literal::
    doppler cli login - This will have you auth against the web UI
    doppler setup - Pick your env location (dev, qa, prd, etc...)

From here any commands you see you would just run :literal:`doppler run -- xxx` where xxx is your normal command to inject env vars automatically.  No need for .env files or exports!

Running on Windows
-------------------
If running Windows 10 or higher would be best to just use WSL and setup an Ubuntu machine and use the terminal from linux there to follow the instructions below.

Setup On Linux/MacOS
---------------------
You will need to setup a virtual environment, you can do that via the below command from your shell/terminal:

.. parsed-literal::
    python -m venv .venv

Then you can activate this via:

.. parsed-literal::
    source .venv/bin/activate

Now you can install the requirements to run Rasa locally

.. parsed-literal::
    pip install -r requirements.txt


Bringing Up Action Server
^^^^^^^^^^^^^^^^^^^^^^^^^^
So in order for Rasa to work properly you also need to run a seperate terminal window.  You will also need to either export the secrets/env vars previously mentioned or can use Doppler.

So if not using doppler for example you would need to run:

.. parsed-literal::
    export NASA_API_KEY=XXX
    export GITHUB_TOKEN=XXX

After having this then you can do the following to run the action server, you can use your existing .venv from rasa.

.. parsed-literal::
    rasa run actions

This should start up an action server and once its up and running you should see some text like the following:

.. parsed-literal::
    2023-02-14 18:14:56 INFO     rasa_sdk.endpoint  - Starting action endpoint server...
    2023-02-14 18:14:56 INFO     rasa_sdk.executor  - Registered function for 'action_apod'.
    2023-02-14 18:14:56 INFO     rasa_sdk.endpoint  - Action endpoint is up and running on http://0.0.0.0:5055

Bringing Up Rasa
^^^^^^^^^^^^^^^^^
Now you can bring up rasa in a seperate terminal since the action server is up.  You can follow the below instructions on how to do this.

.. parsed-literal::
    source .venv/bin/activate
    rasa shell

This will allow you to interact with the chatbot from the shell.  If you wanted to just run rasa and interact with it via API calls, etc you woul do:

.. parsed-literal::
    rasa run --cors '*' --debug


Interacting With Bot
---------------------
So if you ran the :literal::`rasa shell` command you should be able to now talk to the bot from the command line, this is the easiest way to test your work and ensure the bot is working correctly.

You can also run commands like below to have it run through the tests dir and check for any issues based on currently maintained tests.

.. parsed-literal::
    rasa test -s tests