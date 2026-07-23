import sys


def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number,
    and the error message.

    :param error: The exception that occurred.
    :param error_detail: The sys module to access traceback details.
    :return: A formatted error message string.
    """
    # Extract traceback details (exception information)
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Get the line number where the exception occurred
    line_number = exc_tb.tb_lineno

    # Build the formatted error message
    error_message = (
        f"Error occurred in python script: [{file_name}] "
        f"at line number [{line_number}]: {str(error)}"
    )

    return error_message


class MyException(Exception):
    """
    Custom exception class that wraps an error with file name and
    line number details for easier debugging.
    """

    def __init__(self, error_message: Exception, error_detail: sys):
        """
        :param error_message: The original exception object.
        :param error_detail: The sys module to access traceback details.
        """
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message