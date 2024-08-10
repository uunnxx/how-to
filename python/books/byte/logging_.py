import os
import platform
import logging


logging_file = './logging.txt'


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    # filename=logging_file,
    filemode='w'
)


logging.debug('Begin')
logging.info('Something')
logging.warning('Ending')
