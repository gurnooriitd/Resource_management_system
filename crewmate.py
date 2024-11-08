'''
    Python file to implement the class CrewMate
'''

import heap
import treasure

def comparatortreasure(a, b):
            if((a.arrival_time + a.size) < (b.arrival_time + b.size)): # then a is on top
                return True
            elif((a.arrival_time + a.size) > (b.arrival_time + b.size)) :
                return False
            elif (a.id <b.id):
                 return True
            else :
                 return False
            
class CrewMate:
    
    def __init__(self):
     
        self.treasureheap = heap.Heap(comparatortreasure, [])
        self.load = 0
        self.lastupdatetime = 0
        self.listtre = []
        pass
    
    def timehelper(self, treasure, arr):      #we are not adding anything to the array , just popped from heap
        current_time = treasure.arrival_time
        last_updated = self.lastupdatetime
        toadd = current_time - last_updated

        while toadd > 0 and self.treasureheap.size > 0 :
            if toadd >= self.treasureheap.arr[0].size:
                processed = self.treasureheap.extract()
                toadd -= processed.size
                last_updated += processed.size
                processed.completion_time = last_updated
                arr.append(processed)
            else:
                self.treasureheap.arr[0].size -= toadd
                last_updated += toadd
                break
        last_updated = max(current_time, last_updated)
        self.lastupdatetime = last_updated
        self.treasureheap.insert(treasure)

