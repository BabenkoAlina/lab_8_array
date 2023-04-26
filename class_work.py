import ctypes

class Array:

    def __init__(self, size) -> None:
        self.size = max(size, 1)
        self._n = 0
        self._array = (ctypes.c_bool * self.size)()
    
    def __length__(self):
        return self._n
    
    def add_item(self, item):
        if self._n < self.size:
            self._array[self._n] = item
            self._n = self._n + 1
        else:
            return "Out of range"

    def get_item(self, idex):
        if idex < self._n:
            return self._array[idex]
        else:
            return "Out of range"
        
    def iterator(self):
        return iter(self._array)
