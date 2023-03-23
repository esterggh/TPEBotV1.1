import os
import pandas as pd
import pkgutil

directory = os.getcwd()
parent = os.path.dirname(directory).replace('\\','/')

class Webhook:
    def __init__(self):
        pass

    def readFiles(keyFile):
        '''
        Read csv and template files
        :param slFile
        :return:
        '''
        accKeyFile = open(keyFile)
        template = pkgutil.get_data("buildABot.Data", 'index_template.js').decode("utf-8") 

        return accKeyFile, template

    def getInfo(slData, accKeyFile, template):
        '''
        Get necessary data from csv files (service account key, firebase url, email)
        '''
        accKey = accKeyFile.read()
        dbURL = slData['Firebase URL'][0]
        slEmail = slData['Email'][0]

        '''
        Replace keywords with extracted values
        '''
        template = template.replace("SERVICEACCOUNTKEYHERE", accKey)
        template = template.replace("DBURLHERE", dbURL)
        template = template.replace("TUTOREMAILHERE", slEmail)

        return template

    def createFulfillment(template):
        '''
        Write updated fulfillment code into destinated files and close files
        '''
        tutorFile = open("./Tutor/For Deployment/index.js", 'w', encoding="utf-8")
        tutorFile.write(template)
        tutorFile.close()
