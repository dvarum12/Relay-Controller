import logging
from systemd import journal

file_log_info = 'log/relay-controller.log'
file_log_error = 'log/relay-controller.err'

with open(file_log_info, "w+"):
    pass
with open(file_log_error, "w+"):
    pass

# create logger with 'Relay-Controller'
logger = logging.getLogger('Relay-Controller')
logger.setLevel(logging.DEBUG)
logger.propagate = False  # Fixes double log to journal

# create file handler which logs even debug messages
ih = logging.FileHandler(file_log_info)
ih.setLevel(logging.DEBUG)

# create file handler with a higher log level
eh = logging.FileHandler(file_log_error)
eh.setLevel(logging.ERROR)

# create journal handler
jh = journal.JournalHandler()
jh.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ih.setFormatter(formatter)
eh.setFormatter(formatter)
jh.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

# add the handlers to the logger
logger.addHandler(ih)
logger.addHandler(eh)
logger.addHandler(jh)
