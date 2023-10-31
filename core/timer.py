from PyQt5.QtCore import QTimer

class Timer:

    scheduled_method = None
    timeout_method = None

    main_timer_interval = 1000
    scheduler_interval = 7000

    def __init__(self):
        self.tic = 0
        self.timer = QTimer(self)
        self.schedule = QTimer(self)
        self.prepare()

    def prepare(self):
        self.timer.timeout.connect(self.timer_tic)
        self.schedule.timeout.connect(self.schedule_tic)
        self.timer.start(self.main_timer_interval)
        self.schedule.start(self.scheduler_interval)

    def timer_tic(self):
        if self.tic > 0:
            self.tic -= 1
        if self.tic == 1 and self.timeout_method != None:
            self.timeout_method()

    def schedule_tic(self):
        if self.scheduled_method != None:
            self.scheduled_method()

    def setup(self):
        self.tic = 5