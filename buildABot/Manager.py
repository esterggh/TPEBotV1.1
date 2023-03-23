import pandas as pd
import os
import shutil
import os.path
import buildABot
import datetime

from buildABot.Database import Database
from buildABot.Entities import Entities
from buildABot.HotTopics import HotTopics
from buildABot.Intents import Intents
from buildABot.WebApp import WebApp
from buildABot.Webhook import Webhook
from buildABot.Menu import Menu
from buildABot.Paraphraser import Paraphraser
from buildABot.Data import Data

directory = os.getcwd()
parent = os.path.dirname(directory).replace('\\','/')

class Manager(Intents, Database, Entities, HotTopics, WebApp, Webhook, Menu, Paraphraser):

    def __init__(self, qaFile, slFile, studentFile, keyFile):
        self.qaFile = qaFile
        self.slFile = slFile
        self.studentFile = studentFile
        self.keyFile = keyFile

    def getData(file):
        """
        Read QAfile and clean the file before using
        :param file: QA_data.xlsx, SL Inputs.xlsx
        :return: [Dataframe] Cleaned file as dataframe
        """
        # Get QAfile and read as dataframe
        df = pd.read_excel(file, dtype=str)
        df.fillna(value='', inplace=True)
        return df
    
    def createParaphrases(self):
        Paraphraser.random_state(1234)
        qaData = Manager.getData(self.qaFile)
        df, df_qn, dfString = Paraphraser.extractData(df=qaData)
        numTrainPara, paraphrases = Paraphraser.paraphrase(dfString=dfString)
        Paraphraser.createNewQAFile(numTrainPara=numTrainPara, paraphrases=paraphrases, df=df, df_qn=df_qn)
        
        return print("\nQA Data ✓\n")
    
    def createIntents(self):
        """
        Executing the different functions to obtain JSON files of all intents
        :return: Display message after successful excution
        """
        data = Manager.getData("./Tutor/QA_Data.xlsx")
        data_with_labels = Intents.getLabels(df=data)
        data_with_labels.to_excel('./Tutor/QA_Paraphrased.xlsx', index=False)  # Update
        result = Intents.getIntents(df=data_with_labels)

        return print("Intents ✓\n")

    def createHotTopics(self):
        """
        Executing the different functions to obtain JSON files of hot topics intents
        :param SLfile: SL inputs.xslx
        :return: Display message after creating hot topics successfully
        """
        data = Manager.getData(self.slFile)
        hotTopics = HotTopics.createHotTopicsIntents(data)

        return print("Hot Topics ✓\n")

    def createEntities(self):
        studentData = Manager.getData(file=self.studentFile)
        slData = Manager.getData(file=self.slFile)

        cleanedStudentData = Entities.cleanStudentID(studentData)
        studentEntity = Entities.createEntity(cleanedStudentData)
        dummyEntity = Entities.createEntity(slData)

        return print("Entities ✓\n")

    def createFulfillment(self):
        slData = Manager.getData(file=self.slFile)
        accKeyFile, template = Webhook.readFiles(keyFile=self.keyFile)
        template = Webhook.getInfo(slData=slData, accKeyFile=accKeyFile, template=template)
        fulfillment = Webhook.createFulfillment(template=template)

        return print("Webhook ✓\n")
    
    def createFirebase(self):
        studentData = Manager.getData(file=self.studentFile)
        slData = Manager.getData(file=self.slFile)

        data, slLogins = Database.getID(data=studentData, slData=slData)
        strings = Database.dataEncryption(data=data, slLogins=slLogins)
        names = Database.sanitiseName(data=studentData)
        firebaseDB = Database.createDBData(strings=strings, names=names)

        return print("Database ✓\n")

    def createWebApp(self):
        df = Manager.getData(file=self.slFile)
        template = WebApp.readFiles()
        data = WebApp.getInfo(df=df, data=template)
        webApp = WebApp.createHTML(data=data)

        return print("WebApp ✓\n")

    def createMenu(self):
        df = Manager.getData("./Tutor/QA_Paraphrased.xlsx")
        Menu.createLearnMenu(df=df)
        Menu.createMainTopicMenu3(df=df)
        Menu.createMainTopicMenu2(df=df)

        return print("Menu ✓\n")
    
    def createZip(self):
        '''
        combine intents into one folder
        '''
        package_dir = os.path.abspath(buildABot.__path__[0])
        src_dir = (package_dir.replace('\\','/')) + '/Data/Default - Learn'

        dir_name = './Chatbot/intents'
        ent_dir = './Chatbot/entities'
        agent_dir = './Tutor'

        zip_name = './Tutor/For Deployment/Agent_IMPORT'

        files = os.listdir(src_dir)
        shutil.copytree(src_dir, dir_name, dirs_exist_ok=True)

        '''
        putting all necessary files to zip for importing to dialogflow
        '''
        shutil.copytree(dir_name, zip_name+'/intents')
        shutil.copytree(ent_dir, zip_name+'/entities')
        shutil.copyfile(agent_dir+'/agent.json', zip_name+'/agent.json')
        shutil.copyfile(agent_dir+'/package.json', zip_name+'/package.json')

        shutil.make_archive(zip_name, 'zip',zip_name)
        shutil.rmtree(zip_name) 

    def createChatbot(self):
        print("Execution started @ ", datetime.datetime.now())
        Manager.createParaphrases(self)
        Manager.createIntents(self)
        Manager.createMenu(self)
        Manager.createHotTopics(self)
        Manager.createEntities(self)
        Manager.createFulfillment(self)
        Manager.createFirebase(self)
        Manager.createWebApp(self)
        print("All files successfully created, prepare for deployment.\n")

        Manager.createZip(self)
        print("Chatbot ready for deployment!\n")
        print("Excution done, exiting...\n")
        print("Execution Ended @ ", datetime.datetime.now())