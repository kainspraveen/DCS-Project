from random import randint

class task:
    #Priority --> LOW => 0; MEDIUM => 1; HIGH =>2
    def __init__(self):
        self.burst=randint(1,100)
        self.priority=randin(0,2)
        self.allocated_res=[]
        self.scheduled=None
        self.remaining_brst=0
        self.waiting_time=0
        self.arrival_time=randint(0,10)

class resource:
    # node => ACTIVE --> 1; ACTIVE STANDBY --> 0
    # in_use if not in use; in_use = 1 if in use;
    def __init__(self):
        self.status=0
        self.scheduled_task=None
        self.in_use=0
