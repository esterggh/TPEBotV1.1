import logging
import buildABot
from buildABot import Manager
import os

class Main:
    chatbot = Manager(qaFile = "./Tutor/QA_Data.xlsx",
                      slFile = "./Tutor/SL Inputs.xlsx",
                      studentFile = "./Tutor/Student List.xlsx",
                      keyFile = "./Tutor/service_account_key.json")
    
    if __name__ == "__main__":
        logger = logging.getLogger()
        try:
            # chatbot.createParaphrases()
            # chatbot.createIntents()
            # chatbot.createMenu()
            # chatbot.createHotTopics()
            # chatbot.createEntities()
            # chatbot.createFulfillment()
            # chatbot.createFirebase()
            # chatbot.createWebApp()
            # print("All files are ready for deployment.\n")
            
            chatbot.createZip()
            print("Chatbot ready for deployment...\n")

        except Exception as e:
            logger.exception("Exception Occured while code Execution: "+ str(e))

