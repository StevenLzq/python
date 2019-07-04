from queue import Queue
import random


def hotPotato(namelist,num):
    simqueue=Queue()
    for name in  namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())#土豆在队头也就是列表尾部
        simqueue.dequeue()

    return simqueue.dequeue()#获胜者

print(hotPotato(['bill','david','susan','jane','kent','brad'],7))

class Printer(object):
    def __init__(self,ppm):
        self.pagerate=ppm
        self.currentTask=None
        self.timeRemaining=0
    def tick(self):
        if self.currentTask !=None:
            self.timeRemaining =self.timeRemaining-1
            if  self.timeRemaining <=0:
                self.currentTask=None

    def busy(self):
        if self.currentTask !=None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages()*60/self.pagerate


class Task(object):
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def simulation(numSeconds,pagesPerMinute):
    labprinter=Printer(pagesPerMinute)#初始化打印机
    printQueue=Queue()#初始化任务队列
    waitingtimes=[]#记录每个任务的等待时间


    for currentSecond in range(numSeconds):#模拟在每180秒随机生成一个一个新任务
        rand_num=random.randrange(1,181)
        if rand_num==1:
            newTask=Task(currentSecond)#产生新任务
            printQueue.enqueue(newTask)#新任务加入等待的对立里面
        if (not labprinter.busy()) and (not printQueue.isEmpty()):#打印机不忙 而且有任务需要做
            nexttask=printQueue.dequeue()#那么就把新任务弹出队列
            waitingtimes.append(nexttask.waitTime(currentSecond))#计算所需时间并存到列表中
            labprinter.startNext(nexttask)#加入新任务

        labprinter.tick()
    average_time=sum(waitingtimes)/len(waitingtimes)
    return average_time

for i in range(10):
    print(simulation(3600,5))



