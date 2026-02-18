class RandomizedSet:

    def __init__(self):
        self.myy=[]
        

    def insert(self, val: int) -> bool:
        if val not in self.myy:
            self.myy.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.myy:
            self.myy.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        import random
        c=random.choice(self.myy)
        return c
