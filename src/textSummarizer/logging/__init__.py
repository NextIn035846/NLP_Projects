import os
import sys
import logging

logging_str = "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"

#Creating the Logs file 
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

#metion the log

logging.basicConfig(
    level=logging.INFO,
    format= logging_str,

    #it will show the error on both means in file as well as in terminal
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("TextSummarizerLogger")


