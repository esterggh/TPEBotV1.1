import logging
import pytransform
from buildABot.dist.Manager import Manager

class Main:
    chatbot = Manager(qaFile = "./Tutor/QA_Data.xlsx",
                      slFile = "./Tutor/SL Inputs.xlsx",
                      studentFile = "./Tutor/Student List.xlsx",
                      keyFile = "./Tutor/service_account_key.json")
    
    if __name__ == "__main__":
        logger = logging.getLogger()
        try:
            chatbot.createChatbot()
        except Exception as e:
            logger.exception("Exception Occured while code Execution: "+ str(e))



