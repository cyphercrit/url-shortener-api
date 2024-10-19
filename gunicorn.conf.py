import multiprocessing

loglevel = 'info'
errorlog = '-'  # Log to stderr
accesslog = '-'  # Log to stdout
workers = multiprocessing.cpu_count() * 2 + 1