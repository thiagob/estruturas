from datetime import datetime

class Timer():

    now = None

    def start(self):
        self.started_time = datetime.now()
        print("**** TIMER STARTED ****")

    def stop(self):
        return datetime.now() - self.started_time