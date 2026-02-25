from collections import defaultdict
class FrequencyTracker:
    def __init__(self):
        self.ans = defaultdict(int)     
        self.hashh = defaultdict(int)   

    def add(self, number: int) -> None:
        old_freq = self.ans[number]
        if old_freq > 0:
            self.hashh[old_freq] -= 1

        self.ans[number] += 1
        new_freq = self.ans[number]
        self.hashh[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        if self.ans[number] == 0:
            return

        old_freq = self.ans[number]
        self.hashh[old_freq] -= 1

        self.ans[number] -= 1
        new_freq = self.ans[number]
        if new_freq > 0:
            self.hashh[new_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.hashh[frequency] > 0
