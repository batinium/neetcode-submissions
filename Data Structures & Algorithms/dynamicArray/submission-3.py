class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * self.capacity

    def get(self, i: int) -> int:
        return self.storage[i]

    def set(self, i: int, n: int) -> None:
        self.storage[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            temp_len = self.size
            self.resize()
            self.storage[temp_len] = n
            
        else:
            self.storage[self.size]=n
        
        self.size +=1

    def popback(self) -> int:
        last = self.storage[self.size - 1]
        self.storage[self.size-1] = None
        self.size -=1
        return last

    def resize(self) -> None:
        self.storage = self.storage + [None] * self.capacity
        self.capacity *=2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
