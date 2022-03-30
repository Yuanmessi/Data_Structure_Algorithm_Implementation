
# 循环队列
class MyCircularQueue:

    def __init__(self, k):
        """
        构造器，初始化循环队列。
        :param k: 队列长度
        """
        self.size = 0
        self.max_size = k
        self.data = [0] * k
        self.front = self.rear = -1

    def enQueue(self, value):
        """
        向循环队列中插入一个元素。如果成功插入则返回真。
        :param value: 插入的元素值
        """
        if self.isFull():
            return False
        if self.rear == -1:
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.data[self.rear] = value
        self.size += 1
        return True

    def deQueue(self):
        """
        从循环队列中删除一个元素。如果成功删除则返回真。
        """
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self):
        """
         从队首获取元素。如果队列为空，返回 -1 。
        """
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self):
        """
        获取队尾元素。如果队列为空，返回 -1 。
        """
        if self.isEmpty():
            return -1
        return self.data[self.rear]

    def isEmpty(self):
        """
        检查循环队列是否为空。
        """
        return self.size == 0

    def isFull(self):
        """
        检查循环队列是否已满。
        """
        return self.size == self.max_size


obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_2 = obj.enQueue(2)
param_3 = obj.enQueue(3)
param_4 = obj.enQueue(4)
param_5 = obj.Rear()
param_6 = obj.isFull()
param_7 = obj.deQueue()
param_8 = obj.enQueue(4)
param_9 = obj.Rear()
print(param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9)
