from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.dq=deque()
        self.k=k
        

    def insertFront(self, value: int) -> bool:
        if len(self.dq)==self.k:
            return False
        else:
            self.dq.insert(0,value)
            return True

    def insertLast(self, value: int) -> bool:
        if len(self.dq)==self.k:
            return False
        else:
            self.dq.append(value)
            return True
        

    def deleteFront(self) -> bool:
        if self.dq:
            self.dq.popleft()
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if self.dq:
            self.dq.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if self.dq:
            return self.dq[0]
        else :
            return -1
        

    def getRear(self) -> int:
        if self.dq:
            return self.dq[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if not self.dq:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if len(self.dq)==self.k:
            return True
        else:
            return False
        


