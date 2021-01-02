import logging
from logging.handlers import TimedRotatingFileHandler
#logging.basicConfig(filename='sample.log',filemode='a', level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d - %(funcName)s')
from python_sample.mydbhandler import MyDBHandler       # custom handler--
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)   # generic --> for medium

#redirect the output to the console
consolerHandler = logging.StreamHandler()       # redirect ur output to console     # flush kart asto -->
consolerHandler.setLevel(logging.INFO)  # only for console
consolerHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(lineno)d - %(funcName)s - %(levelname)s - %(message)s '))


#redirect the output to --> file --
fileHandler = logging.FileHandler(filename='sam.log',mode='a')      # grow hoel file--> may create a problem in larger applications
fileHandler.setLevel(logging.INFO)  # this is only for file handler
fileHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d - %(funcName)s'))


#redirect to the file --> bt  -> time basis vr..

timeFileHandler = TimedRotatingFileHandler(filename='abc.log',when='M',backupCount=10)
timeFileHandler.setLevel(logging.INFO)  # this is only for file handler
timeFileHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d - %(funcName)s'))

#redirect ur logs to db handler --
dbHandler = MyDBHandler()
dbHandler.setLevel(logging.INFO)  # this is only for file handler
dbHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d - %(funcName)s'))


logger.addHandler(consolerHandler)  # console
logger.addHandler(fileHandler)      #sam.log --> ekach file
logger.addHandler(timeFileHandler)  # abc.log --> per minute new file-->
logger.addHandler(dbHandler)      # db handler -->

import time

def function_one():

  for item in range(1000000):
        logger.info('This is info message-20')
        logger.debug('This is debug Message-10')
        logger.warning('This is warning message-30')
        logger.critical('This is critical message-50')
        logger.error('This is error message-40')
        time.sleep(2) # every 2 seconds --> ek iterations ---> 30 iteration nntr --> 1 file generate..
        logger.info('Iteration NUmber :'+str(item))

            #to transfer -- files from one env to another -->   windows-linux -- linux to windows -- w-w --> l-l
#winscp --> GUI
#putty--scp --> command line utility
#ipmessager --> network
if __name__ == '__main__':
    function_one()