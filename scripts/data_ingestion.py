import yfinance as yf
import logging

# Get the logger specified in the file
logger = logging.getLogger(__name__)

tracker = "AAPL"
data = yf.download(tracker)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

if data.shape[0]==0:
    logger.error("Data empty")
else:
    try:
        file_path = r"./data/{}.csv".format(tracker)
        data.to_csv(file_path)
        print(f"Data saved to {file_path}")
    except Exception as ex:
        print(ex)