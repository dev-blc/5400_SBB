
import threading


class Miner:
    def __init__(self):
        thread = threading.Thread(target=self.run())
        thread.start()

    def run(self):
        