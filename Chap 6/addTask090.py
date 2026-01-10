from celery import Celery

# Initialize Celery with RabbitMQ broker and RPC backend to store results
app = Celery('addTask', 
             broker='amqp://guest@localhost//')

# Logic from your main_code.py
def gcd_logic(a, b):
    while b != 0:
        a, b = b, a % b
    return a

@app.task
def add(x, y):
    """Simple addition task."""
    return x + y

@app.task
def calculate_gcd(a, b):
    """Calculates GCD using a background worker."""
    return gcd_logic(a, b)

@app.task
def calculate_lcm(a, b):
    """Calculates LCM using a background worker."""
    res_gcd = gcd_logic(a, b)
    return (a * b) // res_gcd