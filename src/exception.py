import sys

from src.logger import logging

def errorMessageDetail(error,errorDetail:sys):
    _,_,exc_tb = errorDetail.exc_info()
    fileName = exc_tb.tb_frame.f_code.co_filename
    errorMessage = "Error occured in Python script name[{0}],line number[{1}],error message[{2}]".format(
        fileName,exc_tb.tb_lineno,str(error)
    )
    return errorMessage

class CustomException(Exception):
    def __init__(self,errorMessage,errorDetail:sys):
        super().__init__(errorMessage)
        self.errorMessage = errorMessageDetail(errorMessage,errorDetail=errorDetail)

    def __str__(self):
        return self.errorMessage

