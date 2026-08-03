class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.storage = [None for _ in range(0,capacity)]

    def get(self, i: int) -> int:
        return self.storage[i]

    def set(self, i: int, n: int) -> None:
        self.storage[i] = n

    def pushback(self, n: int) -> None:
        if self.size < self.capacity:
            self.storage[self.size] = n
        else:
            self.resize()
            self.storage[self.size]= n
        self.size +=1

    def popback(self) -> int:
        lastitem = self.storage[self.size-1] 
        self.storage[self.size - 1] = None
        self.size -=1
        return lastitem

    def resize(self) -> None:
        self.capacity *=2
        self.storage = self.storage + [None for _ in range(0,len(self.storage))]
        

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
