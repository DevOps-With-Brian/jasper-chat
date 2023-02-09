# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import requests
import os
from dotenv import load_dotenv

load_dotenv()

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAPOD(Action):

    def name(self) -> Text:
        return "action_apod"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # NASA APOD API endpoint
        api_url = "https://api.nasa.gov/planetary/apod"
        public_apod_url = "https://apod.nasa.gov/apod/"


        # API key
        api_key = os.getenv("API_KEY")
        print(api_key)

        # Make a GET request to the endpoint with the API key
        response = requests.get(api_url + "?api_key=" + api_key)

        # Check the status code of the response
        if response.status_code == 200:
            # If the status code is 200 (OK), get the JSON data from the response
            data = response.json()

            # Print the title and explanation of the APOD
            jasper_response = "Sure, here is a link to the Astronomy Picture of the Day, today's picture is of: {0} and you can see it at {1}".format(data["title"],public_apod_url)
            print("Title:", data["title"])
            print("Link to Picture & Full Explanation:", public_apod_url)
            dispatcher.utter_message(text=jasper_response)

        else:
            # If the status code is not 200 (OK), print an error message
            jasper_err = "Sorry, I wasn't able to hit the NASA API at this time."
            print("An error occurred while fetching the data:", response.text)
            dispatcher.utter_message(text=jasper_err)

        return []
