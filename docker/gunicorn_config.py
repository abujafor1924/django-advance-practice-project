import multiprocessing

# Binding
bind = "0.0.0.0:8000"

# Worker Options
# Formula: (2 x $num_cores) + 1
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
timeout = 120
keepalive = 2

# Logging
accesslog = "-"  # Log to stdout
errorlog = "-"   # Log to stderr
loglevel = "info"

# Process Naming
proc_name = "bellevie_gunicorn"
