class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise  ValueError("Invalid Input")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookies = ""
        for i in range(self.size):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        new_n = self.size + n
        if new_n <= self.capacity:
            self.size = new_n
        else:
            raise ValueError("No room")

    def withdraw(self, n):
        new_n = self.size - n
        if new_n >= 0:
            self.size = new_n
        else:
            raise ValueError("Not enough cookies")
        

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
    

