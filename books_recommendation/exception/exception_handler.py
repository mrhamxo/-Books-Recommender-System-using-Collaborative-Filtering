import sys

class AppException(Exception):
    """
    Custom exception class for handling application-level errors with detailed context.
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Constructor for AppException.

        Args:
            error_message (str): The original exception message.
            error_detail (sys): The sys module (used to get exception context).
        """
        super().__init__(error_message)
        self.error_message = AppException.error_message_detail(error_message, error_detail)

    @staticmethod
    def error_message_detail(error_message, error_detail: sys):
        """
        Generates a detailed error message including file name and line number.

        Args:
            error_message (str): The original exception message.
            error_detail (sys): The sys module (used to extract traceback).

        Returns:
            str: Formatted error message with context.
        """
        _, _, exc_tb = error_detail.exc_info()
        
        #extracting file name from exception traceback
        file_name = exc_tb.tb_frame.f_code.co_filename
        
        line_number = exc_tb.tb_lineno
        return f"Error in file [{file_name}] at line [{line_number}]: {str(error_message)}"

    def __str__(self):
        """
        String representation of the exception.

        Returns:
            str: The detailed error message.
        """
        return self.error_message

    def __repr__(self):
        """
        Developer-friendly string representation.

        Returns:
            str: Class name and error message.
        """
        return f"{self.__class__.__name__}('{self.error_message}')"
