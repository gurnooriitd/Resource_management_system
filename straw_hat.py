import crewmate
import heap
import treasure

def comparatorcrew(a, b):
            if(a.load < b.load):
                return True
            else:
                return False
            
class StrawHatTreasury:   
    def __init__(self, m):
        
        self.arr = [] #the main crewmates array
        self.treasure_list = []
        self.count_tre = 0
        self.noofcrewmate = m
        for i in range (0,m):
            temp = crewmate.CrewMate()
            self.arr.append(temp)
        self.heapcrewmates = heap.Heap(comparatorcrew, self.arr) 
        
    def add_treasure(self, tre:treasure.Treasure):
        
        leastloaded = self.heapcrewmates.extract()
        time = tre.arrival_time
        size = tre.size

        if leastloaded.load > time:   
            leastloaded.load += size
        else :
            leastloaded.load = (size + time)

        self.count_tre += 1
        self.treasure_list.append(tre)
        leastloaded.listtre.append(tre)  
        self.heapcrewmates.insert(leastloaded)

    def get_completion_time(self):
        ans = []
        
        if self.noofcrewmate <= self.count_tre:
            for crew_mate in self.heapcrewmates.arr:
                if not crew_mate.listtre:
                    continue
                
                crew_mate.lastupdatetime = 0

                for x in crew_mate.listtre:
                    #this will make a new treasure and then add 
                    # Print(crew_mate)
                    crew_mate.timehelper(treasure.Treasure(x.id, x.size, x.arrival_time), ans)

                temp = crew_mate.lastupdatetime
                
                while crew_mate.treasureheap.size > 0:
                    top_ele = crew_mate.treasureheap.extract()
                    if top_ele and top_ele.completion_time is None:
                        temp += top_ele.size
                        temp1 = treasure.Treasure(top_ele.id, top_ele.size, top_ele.arrival_time)
                        temp1.completion_time = temp
                        ans.append(temp1)
                    elif top_ele:
                        ans.append(top_ele)
                

        else:
            for treasure_item in self.treasure_list:
                treasure_item.completion_time = treasure_item.arrival_time + treasure_item.size  # no load case
                ans.append(treasure_item)

        ans.sort(key=lambda x: x.id)
        return ans

    

