import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('email_service')

file_handler = logging.FileHandler('service.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
