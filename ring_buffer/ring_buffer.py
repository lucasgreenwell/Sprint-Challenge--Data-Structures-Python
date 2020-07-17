class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.ages= {}
        self.number_of_things = 0

    def append(self, item):
        self.number_of_things += 1
        if self.capacity == len(self.storage):
            print(self.ages.values())
            print(self.storage)
            oldest_existing = self.ages[self.number_of_things - self.capacity]
            index_to_kill = self.storage.index(oldest_existing)
            self.storage.remove(oldest_existing)
            self.storage.insert(index_to_kill, item)
            self.ages[self.number_of_things] = item
        else:
            self.storage.append(item)
            self.ages[self.number_of_things] = item


    def get(self):
        return self.storage