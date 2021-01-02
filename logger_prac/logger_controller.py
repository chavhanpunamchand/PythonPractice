from py_logging.python_sample.app_queries import *
from py_logging.python_sample.product_info import Product
from py_logging.python_sample.db_util import get_connection,close_resources
import logging
                #level --> WARNING
logging.basicConfig(filename='check.log',filemode='a',level=logging.INFO,
                    format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')

def m1():
   logging.info('This is info message-20')
   logging.debug('This is debug Message-10')
   logging.warning('This is warning message-30')
   logging.critical('This is critical message-50')
   logging.error('This is error message-40')



if __name__ == '__main__':
   m1()

#import sys
#sys.exit(0)
