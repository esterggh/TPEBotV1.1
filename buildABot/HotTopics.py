import json
import os
directory = os.getcwd()
parent = os.path.dirname(directory).replace('\\','/')

class HotTopics:
    def __init__(self):
        import pandas as pd

    def write_file_json(file, data):
        with open(file, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

    def getIntentTemplate():
        """
        Dialogflow's intent template, structured for hot topics
        :return: JSON template of hot topics intent
        """
        return {
            "id": "9aea7e9d-678d-4bbb-ab13-ebf605dcb704",
            "name": "Log In - Sentiment (Awesome)",
            "auto": True,
            "contexts": [
                "loginID"
            ],
            "responses": [
                {
                    "resetContexts": False,
                    "action": "",
                    "affectedContexts": [
                        {
                            "name": "loginID",
                            "lifespan": 50
                        }
                    ],
                    "parameters": [
                        {
                            "id": "5011400b-03a5-4f8c-bf92-859cef03e8a3",
                            "name": "loginID",
                            "required": False,
                            "dataType": "@LoginID",
                            "value": "#loginID.loginID",
                            "defaultValue": "",
                            "isList": False,
                            "prompts": [],
                            "promptMessages": [],
                            "noMatchPromptMessages": [],
                            "noInputPromptMessages": [],
                            "outputDialogContexts": []
                        }
                    ],
                    "messages": [
                        {
                            "type": "0",
                            "title": "",
                            "textToSpeech": "",
                            "lang": "en",
                            "speech": [
                                "Yay, Keep it up! 🥳 \n\nFeel free to explore the menu below, or you can ask me anything about the subject, I would love to help!"
                            ],
                            "condition": ""
                        },
                        {
                            "type": "0",
                            "title": "",
                            "textToSpeech": "",
                            "lang": "en",
                            "speech": [
                                "Current Hot Topics:"
                            ],
                            "condition": ""
                        },
                        {
                            "type": "4",
                            "title": "",
                            "payload": {
                                "richContent": [
                                    [
                                        {
                                            "options": [  # FAQ HERE
                                            ],
                                            "type": "chips"
                                        }
                                    ]
                                ]
                            },
                            "textToSpeech": "",
                            "lang": "en",
                            "condition": ""
                        },
                        {
                            "type": "0",
                            "title": "",
                            "textToSpeech": "",
                            "lang": "en",
                            "speech": [
                                "Menu:"
                            ],
                            "condition": ""
                        },
                        {
                            "type": "4",
                            "title": "",
                            "payload": {
                                "richContent": [
                                    [
                                        {
                                            "type": "chips",
                                            "options": [
                                                {
                                                    "text": "See Topics"
                                                }
                                            ]
                                        }
                                    ]
                                ]
                            },
                            "textToSpeech": "",
                            "lang": "en",
                            "condition": ""
                        }
                    ],
                    "speech": []
                }
            ],
            "priority": 500000,
            "webhookUsed": False,
            "webhookForSlotFilling": False,
            "fallbackIntent": False,
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }

    def getTextPayload():
        return {"text": "suggested topic"}

    def createHotTopicsIntents(df):
        """
        Retrieve pre-set hot topics and produce hot topics intents accordingly
        """
        hotTopicsIntents = [] # Create empty list

        for x, rows in df.iterrows():
            hotTopicResponse = HotTopics.getIntentTemplate()
            hotTopicTextPayload = HotTopics.getTextPayload()

            hotTopicResponse.pop("id", None)
            hotTopicTextPayload["text"] = rows["FAQ"] # Put in hot topics chosen into respective placeholder
            hotTopicsIntents.append(hotTopicTextPayload)

        # Place collated hot topics text paload into the intent template placeholder
        hotTopicResponse["responses"][0]["messages"][2]["payload"]["richContent"][0][0]["options"] = hotTopicsIntents

        '''
        Standard intent name and training phrases of intent that display hot topics
        '''
        intentNames = ["Log In - Sentiment (Awesome)", "Log In - Sentiment (Doing Fine)",
                       "Log In - Sentiment (It\u0027s been a rough week)", "Log In - Sentiment (Still Hanging There)"]
        textResponse = [
            "Yay, Keep it up! 🥳 \n\nFeel free to check out the hot topics or explore the menu below! You can also ask me anything about the subject, I would love to help!",
            "That\u0027s good to hear! 😃 \n\nFeel free to check out the hot topics or explore the menu below! You can also ask me anything about the subject, I would love to help!",
            "Hang on there and don\u0027t give up! Tomorrow will be better. 😉 \n\nFeel free to check out the hot topics or explore the menu below! You can also ask me anything about the subject, I would love to help!",
            "Keep pushing and it will get better! 🤗 \n\nFeel free to check out the hot topics or explore the menu below! You can also ask me anything about the subject, I would love to help!"]

        for i in range(4): # loop through all hot topics intents
            hotTopicResponse["name"] = intentNames[i]
            hotTopicResponse["responses"][0]["messages"][0]["speech"][0] = textResponse[i]
            HotTopics.write_file_json("./Chatbot/intents/{}.json".format(intentNames[i]), hotTopicResponse)

        
