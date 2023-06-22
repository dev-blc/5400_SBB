import threading
import time
from app2 import App2

# Create an instance of App2
app2 = App2()

# Define a function to be called on a separate thread for the infinite loop
def infinite_loop():
    while True:
        app2.infinite_task()
        if app2.should_terminate():
            break

# Define a function to be called on a separate thread for executing additional functions
def execute_additional_functions():
    app2.function4()
    app2.function5()

# Start a new thread for the infinite loop
infinite_thread = threading.Thread(target=infinite_loop)
infinite_thread.start()

# Call other functions on App2 from app1.py in the main thread
print("wtf")
app2.function1()

# Start a new thread for executing additional functions
additional_thread = threading.Thread(target=execute_additional_functions)
additional_thread.start()

# Wait for the infinite thread to terminate gracefully
