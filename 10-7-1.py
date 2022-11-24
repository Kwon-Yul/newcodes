class EvenCounter:
    def __init__(self, n=0):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n<10:
            t = self.n
            self.n +=2
            return t
        raise StopIteration
    
mycounter = EvenCounter()
for i in mycounter:
    print(i,end=' ')