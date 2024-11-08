'''
Python Code to implement a heap with general comparison function
'''
# class PriorityQueueBase:
#     # ”””Abstractbaseclassforapriorityqueue.”””
#     class Item:
#     # ”””Lightweightcompositetostorepriorityqueueitems.”””
#         __slots__ = '_key' , '_value'

#         def __init__(self,k,v):
#             self._key = k
#             self._value=v

#         def __lt__ (self,other):
#             return self._key<other._key #compare itemsbasedontheirkeys

#     def is_empty(self): #concretemethodassumingabstract len
#     # ”””ReturnTrueifthepriorityqueueisempty.”””
#         return len(self)==0

class Heap():
    '''
    Class to implement a heap with general comparison function

    '''
    def __len__(self):
        return len(self.arr)

    def is_empty(self):
        return len(self) == 0
   
    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j+1

    def _right(self, j):
        return 2*j+2
    
    def _has_left(self, j):
        return self._left(j)<len(self.arr) #indexbeyondendof list?
 
    def _has_right(self, j):
        return self._right(j)<len(self.arr) #indexbeyondendof list?

    def _swap(self, i, j):
    #Swap the elements at indices i and j of array
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j>0 and self.comparator(self.arr[j],self.arr[parent]):
            self._swap(j,parent)
            self._upheap(parent) #recuratpositionofparent

    def _downheap(self, j):
        if self._has_left(j):
            left=self._left(j)
            small_child=left #althoughrightmaybesmaller
            if self._has_right(j):
                right=self._right(j)
                if self.comparator(self.arr[right],self.arr[left]):
                    small_child=right
            if self.comparator(self.arr[small_child],self.arr[j]):
                self._swap(j, small_child)
                self._downheap(small_child)
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.arr = []
        self.comparator = comparison_function
        self.size = 0
        for x in init_array:
            self.insert(x)
        pass
        
    def insert(self,value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.size +=1
        self.arr.append(value)
        self._upheap(len(self.arr)-1)
        pass
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if self.size == 0:
            return None
            
        item = self.arr[0] #andremove itfromthelist;
        self._swap(0, len(self.arr)-1) #putminimumitemattheend
        self.arr.pop()
        self.size -= 1
        self._downheap(0) #thenfixnewroot
        return item
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if self.size == 0:
            return None
        else :
            return self.arr[0]