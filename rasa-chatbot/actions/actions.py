from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):

    def name(self) -> str:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        dispatcher.utter_message(text="Hello, world!")

        return []


class ActionFetchData(Action):

    def name(self) -> str:
        return "action_fetch_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        # Here you would add logic to fetch data from an API or database
        data = "Sample data fetched from an external source."
        dispatcher.utter_message(text=data)

        return []