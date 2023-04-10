import heapq

class Process:
    def _init_(self, name, priority, burstTime):
        self.name = name
        self.priority = priority
        self.burstTime = burstTime
        self.remainingTime = burstTime
        self.quantum = 2

    def execute(self):
        if self.remainingTime > self.quantum:
            print("Executing", self.name, "for", self.quantum, "units of time")
            self.remainingTime -= self.quantum
        else:
            print("Executing", self.name, "for", self.remainingTime, "units of time")
            self.remainingTime = 0

    def isFinished(self):
        return self.remainingTime == 0

    def hasHigherPriority(self, other):
        return self.priority < other.priority

class Scheduler:
    def _init_(self):
        self.queue1 = []
        self.queue2 = []
        self.quantum = 2

    def addProcess(self, name, priority, burstTime):
        process = Process(name, priority, burstTime)
        heapq.heappush(self.queue1, (priority, process))

    def run(self):
        while self.queue1 or self.queue2:
            if self.queue1:
                priority, current = heapq.heappop(self.queue1)
                print("Running process", current.name, "from Queue 1 with priority", current.priority)
                current.execute()
                if current.isFinished():
                    print("Process", current.name, "finished")
                else:
                    self.queue2.append(current)
            else:
                current = self.queue2.pop(0)
                print("Running process", current.name, "from Queue 2 with priority", current.priority)
                current.execute()
                if current.isFinished():
                    print("Process", current.name, "finished")
                else:
                    self.queue2.append(current)

scheduler = Scheduler()
scheduler.addProcess("P0", 0, 4)
scheduler.addProcess("P1", 1, 3)
scheduler.addProcess("P2", 3, 7)
scheduler.addProcess("P3", 2, 4)
scheduler.run()
