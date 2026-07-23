# import logging
# import src.logger  # adjust this import to match your actual folder structure

# logger = logging.getLogger(__name__)

# logger.debug("This is a debug message.")
# logger.info("This is an info message.")
# logger.warning("This is a warning message.")
# logger.error("This is an error message.")
# logger.critical("This is a critical message.")

# print(f"Check your log file at: {src.logger.log_file_path}")


# # below code is to check the exception config
# import sys
# import logging

# from src.exception import MyException
# from src.logger import logging  # ensures logger is configured (adjust path if needed)

# try:
#     a = 1 + 'Z'
# except Exception as e:
#     logging.error("Exception occurred: %s", e)
#     raise MyException(e, sys) from e

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()