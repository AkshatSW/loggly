import logging
from loggly.handlers import HTTPSHandler

# Replace 'YOUR_CUSTOMER_TOKEN' with your actual Loggly customer token
LOGGLY_TOKEN = '0674d822-120a-4c65-ac1c-39b4256faa22'

# Set up the logger
logger = logging.getLogger('LogglyLogger')
logger.setLevel(logging.INFO)

# Create the HTTPSHandler instance
https_handler = HTTPSHandler(url=f'https://logs-01.loggly.com/inputs/{LOGGLY_TOKEN}/tag/python')

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
https_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(https_handler)

# Your application code here
# ...

# Example log messages
logger.info('Application has started')
logger.warning('An example warning message')
logger.error('An example error message')

# Run your application...

