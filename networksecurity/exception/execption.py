import sys
from networksecurity.logging import logger

import sys

class NetworkSecurityException:
    def __init__(self, error_message, error_details: sys):
        # Store the error message provided when raising the exception
        self.error_message = error_message

        # Extract exception information using sys.exc_info(), which returns a tuple:
        # (type, value, traceback). Here we ignore type and value with underscores.
        _, _, exc_tb = error_details.exc_info()

        # Get the line number where the exception occurred from the traceback object
        self.lineno = exc_tb.tb_lineno

        # Get the name of the file where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        
if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
           raise NetworkSecurityException(e,sys)