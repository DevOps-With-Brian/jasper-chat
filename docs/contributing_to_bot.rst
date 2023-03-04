********************
Contributing To Bot
********************
So if you want to contribute to the bot to add new responses or things that Jasper can answer you can easily do this modifying YAML files, you don't even need to know how to code!

The below sections will outline the process to add new intents and responses to the chatbot.


Adding Intents
----------------
So this bot framework works off NLU processing so we have to give it training examples in order to have it start learning how to clasify text properly.

Currently the NLU training data resides in the `data/nlu.yml` file.

You can see the current format of a new intent which follows this format as seen below:

.. parsed-literal::
    - intent: out_of_scope
      examples: |
        - Who's the US President?
        - What is 2 + 2?
        - How do I code in python?
        - what is world of warcraft
        - who is marilyn monroe?

So as you can see here this is one intent that is under the bigger nlu: section.  You can follow the same logic and add your own with your own custom intent name which needs to follow abc_blah if longer namewise.
The examples are ways users might ask the bot to hit the intent you are trying to classify and respond to.

After adding this in you can move to the next section of setting up the response for your intent.

Adding Responses
-----------------
Typically you will just want a text based response to your question coming into the bot that is being classified, you can also do custom actions for external python code but that will be documented later.

Inside the `domain.yml` file you will see a top level intents section you need to add your new intent to:

.. parsed-literal::
    intents:
    - out_of_scope

After doing this you can add the new response for when this intent is classifed by adding a new phrase under the responses: section.

.. note::
    Please note the utterances/responses names need to start with utter_xxx.


Update Stories
---------------
After setting up your `domain.yml` file with your new intent and utterance you can now setup the story to teach the bot the ways the users might interact with it to get to your intent.

For example we have the greeting intent story seen below, this is a very basic one, but you would want to expand on this as seen from other stories in the file for an example.

.. parsed-literal::
    - story: greeting
      steps:
      - intent: greet
      - action: utter_greet

So this is 1 story that tells the bot, someone will greet the bot then I want you to run the action utter_greet so it would respond with that.  You would just follow this same logic to setup your story depending on how the user might interact with the bot.

After doing a few of these then you want to also setup the test stories as seen in the next section.


Add Test Stories
^^^^^^^^^^^^^^^^^
The test stories are located in the `tests` dir and atm are only in test_stories.yml.

You can see examples here on how this works, but its very similar to the normal stories except you are giving it the input the user might ask to test the bot to make sure it can classify the text correctly.

.. parsed-literal::
    - story: basic greeting
      steps:
      - user: |
          hello there!
        intent: greet
      - action: utter_greet

So as seen here, the user would ask the bot `hello there` and the bot should classify this as `greet` and then call the `utter_greet` response, if it doesn't this will fail in the tests.

Pushing Up Changes
-------------------
Now you have your files but we need to commit them and push them up for a PR review to be added to the bot, the below sections will outline this.


Conventional Commits
^^^^^^^^^^^^^^^^^^^^^^
This repo uses `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ for all its work, you will need to adhere to this and make sure you use a conventional commit.

This might look something like:

.. parsed-literal::
    git commit -m "feat: adding phrase abc123 to bot"

This is a conventional commit and will pass initial PR checks, ensure you use these types of commits.


Testing Bot Locally
^^^^^^^^^^^^^^^^^^^^
Ensure you have tested via the :literal:`rasa shell` command to make sure your bot works as expected and also run :literal:`rasa test -s tests` and then check the :literal:`results/failed_test_stories.yml` for any failed stories.


Adding Code & Pushing
^^^^^^^^^^^^^^^^^^^^^^^
Now you can add your files like seen below and push and then create a `Pull Request <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_ and it will be reviewed.

This example below will show creating a local branch off main and adding your code and then pushing:

.. parsed-literal::
    git checkout -b feature/add-blah-intent
    git add . ## This should only add the files you modified
    git commit -m "feat: adding phrase abc123 to bot"
    git push origin HEAD

This should then give you prompt when you go to the repo in GitHub to create a PR and it will be reviewed and merged.  Upon merging it will auto update the bot via CI/CD processes.