**************
Initial Setup
**************
This section covers how to initially setup Jasper locally and test the bot and interact with it.


Pre-Req's
-----------
This requires a few things to work.  You need to have `Python3 <https://www.python.org/downloads/>`_ installed first off.  At the time of writing this, it has been tested with 3.8.10.  It should work with newer versions per Rasa's requirement.  Please ensure you have python before continuing.

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
So in order for Rasa to work properly you also need to run a seperate terminal window.  You will also have to generate an API Key from Nasa's free API.

You will export this via a export var called `API_KEY` which is basically the Nasa API key for the APOD trigger.

This can be generated at `Nasa API <https://api.nasa.gov/>`_.

After having this then you can do the following to run the action server, you can use your existing .venv from rasa.

.. parsed-literal::
    export API_KEY=xxxxx
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