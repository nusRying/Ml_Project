import sys

def error_message_detail(error , error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    
    error_message = f"Error: {error} \n Error Detail: {error_detail} \n Error Line: {exc_tb.tb_lineno}"
    file_name = exc_tb.tb_frame.f_code.co_filename
    return error_message, file_name

class customException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
    
    def __str__(self):
        return self.error_message