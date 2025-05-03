import logging
import os
from datetime import datetime


log_folder = os.path.join(os.getcwd(), "logs")
os.makedirs(log_folder, exist_ok=True)

#define  log format
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#create log folder if doesn't exit
log_file_path = os.path.join(log_folder, log_file)

#define  a dedicated logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  

#los format
formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")

#File writer
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)

#display in console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

#adding handler(if it doesn't exit)
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

