###
#addTask.py : RUN the AddTask example with 
###

import Celery.addTask038 as addTask038
import time

if __name__ == '__main__':
    print("--- Sending Tasks to Celery Worker ---")
    
    # Send tasks to the broker using .delay()
    res_add = addTask038.add.delay(5, 5)
    res_gcd = addTask038.calculate_gcd.delay(48, 18)
    res_lcm = addTask038.calculate_lcm.delay(12, 15)

    # Wait for the results to be ready
    print("Waiting for results...")
    while not res_lcm.ready():
        time.sleep(0.5)

    # Retrieve and print the results
    print(f"Add Result (5+5): {res_add.get()}")
    print(f"GCD Result (48, 18): {res_gcd.get()}")
    print(f"LCM Result (12, 15): {res_lcm.get()}")
    print("--- All Tasks Completed ---")