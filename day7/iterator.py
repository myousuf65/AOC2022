# iterator vs iterable

# 1. if something is iterable, it should have __iter__() method
# 2. iterator has a state so that it knows where it is in an iteration
# 3. iterator gets their next value using the next() method

# Loop using iterator
li = ['alice', 'bob', 'peter']
iterator = iter(li)

for i in range(len(li)):
    next(iterator)

# Changing item of a list    
li = ['alice', 'bob', 'peter']

for i in range(len(li)):
    if li[i] == 'alice':  
        li[i] = 'khan' 




# class example
class MyRange:
    def __init__(self, start, end) :
        self.value = start
        self.end = end


    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
            
        return None



