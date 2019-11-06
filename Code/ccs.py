from imports import *
import pandas as pd
from random import randint

class ccs:
    def __init__(self):
        self.no_resources=10
        self.available_res=10
        self.failure=0
        self.repair=0
        self.tasks=[]
        self.resources=[]
        self.index=0
        self.timer=0

    def initializer(self, n):

        #initializing Tasks
        for i in range(n):
            self.tasks.append(task())

        #initializing Resources
        for i in range(self.no_resources):
            self.resources.append(resource())


    def resourceManager(self,task):
        if(task.priority == 2):
            res=self.failure//self.repair
            start=index
            if(self.index<no_resources):
                for i in range(index, res):
                    self.resources[i].in_use = 1
                self.index=res-1
                end=index
                task.allocated_res=[start,end]
                return True
            else:
                return False
        else:
            index=-1
            for i in range(no_resources):
                if(self.resources[i].status != 1):
                    index=i
                    break
            if(index!=-1):
                task.allocated_res=[index,index+1]
                self.available_res-=1
                return True
            else:
                return False

    def task_arrival(self,task):
        if(task.priority == 2):
            if(self.resourceManager(task)):
                self.timer+=task.burst
                task.waiting_time=timer-task.burst
                self.resources[task.allocated_res[0]].status=1
                task.scheduled=task.allocated_res[0]
                self.resources[task.allocated_res[0]].scheduled_task=task
                for i in range(task.allocated_res[0]+1,task.allocated_res[1]):
                    self.resources[i].status=0
                self.taskDeparture(task)
                self.available_res-=1
                return True
            else:
                retrun False
        else:
            # Doubt in this part
            if(self.resourceManager(task)):
                self.timer+=task.burst
                task.waiting_time=timer-task.burst
                task.scheduled=task.allocated_res[0]
                self.resources[task.allocated_res[0]].scheduled_task=task
                self.taskDeparture(task)
                return True
            else:
                return False



    def nodeFail(self, node):               #try randomly Failing node to be parallel using thread
        running_task=node.scheduled_task    #for better simulation
        failed_status=node.status
        self.resources.remove(node)
        if(failed_status == 1):
            if(self.available_res > 0):
                for i in range(10):
                    if(self.resources[i].status==0):
                        running_task.scheduled = self.resources[i]
                        self.resources[i].scheduled_task = running_task
                        break
        else:
            if(node.scheduled_task != None):
                for i in range(len(self.tasks)):
                    if(self.tasks[i]==running_task);
                    self.tasks[i].scheduled=None
                    self.tasks[i].allocated_res=[]
                for i in range(len(self.resources)):
                    if(self.resources[i]==node):
                        self.resources[i].scheduled_task=None


    def taskMigration(self, task):


    def taskReconsideration(self, task):
        pass

    def taskDeparture(self, task):
        pass

    def ccs(self):
        pass

#main function
def main():
    pass


if __name__ == '__main__':
    main()
