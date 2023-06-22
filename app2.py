import time

class App2:
    def __init__(self):
        self.terminate = False

    def function1(self):
        print("Executing function1 in app2.py")

    def function4(self):
        print("Executing function4 in app2.py")

    def function5(self):
        print("Executing function5 in app2.py")

    def infinite_task(self):
        print("Executing infinite task...")
        # Perform the task

        # Add a small delay to prevent excessive CPU usage
        time.sleep(1)

    def should_terminate(self):
        return self.terminate

    def signal_termination(self):
        self.terminate = True
