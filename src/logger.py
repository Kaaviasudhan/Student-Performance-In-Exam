# mainly used and helps log purpose to track the exception/error to be note down

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"		# file name format as: date.log file
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)			        # Log file created inside the current working directory (cwd) followed with given file naming format
os.makedirs(logs_path,exist_ok=True)					            # If folder and file exsist, keep appending the file in the cwd

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)				

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

if __name__ =="__main__":
	logging.info("Logging has started")
