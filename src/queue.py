

class QueueNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self._next = None
        self._prev = None

    def get(self):
        return [self.key, self.value]



class Queue:

    def __init__(self):
        self.first = None
        self.last  = None

    def add(self, key, value):
        """ Add key value into the QueueNode and
            return reference to QueueNode
        """
        temp = QueueNode(key, value)
        if self.first is None:
            self.first = temp
            self.last  = temp
        else:
            self.last._next = temp
            temp._prev      = self.last
            self.last       = temp

        return temp

    def remove(self):
        """ Remove last node in the list and return key, value pair
        """
        ret = [None, None]
        if self.last is None:
            return ret
        
        ret = self.last.get()
        if self.first == self.last:
            # List has only one element
            self.first = None
            self.last  = None
        else:
            deleteNode      = self.last
            self.last       = deleteNode._prev
            self.last._next = None
            deleteNode._prev= None

        return ret

    def access(self, node):
        """
        put given node to the head of the queue
        and rearrange the rest of the queue
        """

        if node is None:
            return
        
        if node == self.first:
            return

        # Remove node from the list
        if node._prev is not None:
            node._prev._next = node._next

        if node._next is not None:
            node._next._prev = node._prev
        
        if node == self.last:
            self.last = self.last._prev

        #Add node to the head of the list
        self.first._prev = node
        node._next       = self.first
        node._prev       = None
        self.first       = node

    def printList(self):
        if self.first is None:
            return
        cur = self.first
        stat = ""
        while cur is not None:
            data = cur.get()
            stat += "["+ str(data[0])+","+str(data[1])+"]|"
            cur = cur._next
        #end of while
        print stat

    def printReverseList(self):
        if self.last is None:
            return
        cur = self.last
        stat = ""
        while cur is not None:
            data = cur.get()
            stat += "["+ str(data[0])+","+str(data[1])+"]|"
            cur = cur._prev
        #end of while
        print stat
    

    
#End of class Queue
def test1():
    print "Test1 Starts"
    queue = Queue()
    print "Add elements to the list"
    queue.add(1, 10)
    queue.add(2, 20)
    queue.add(3, 30)
    queue.printList()
    print "Remove element"
    elm1 = queue.remove()
    elm2 = queue.remove()
    queue.remove()
    print "Removing from empty list"
    queue.remove()
    queue.printList()
    print "2nd removed element", elm2


def test2():
    print "Test2 Starts"
    queue = Queue()
    print "Build List"
    queue.add(1, 10)
    queue.add(2, 20)
    queue.add(3, 30)
    queue.add(4, 50)
    queue.printList()
    print "Reverse List"
    queue.printReverseList()

def test3():
    print "Test3 Starts"
    queue = Queue()
    nd1 = queue.add(1,10)
    nd2 = queue.add(2,20)
    nd3 = queue.add(3, 30)
    nd4 = queue.add(4, 40)
    nd5 = queue.add(5, 50)
    print "Original List"
    queue.printList()
    print "Accessing nd3"
    queue.access(nd3)
    print "Rearranged List"
    queue.printList()
    print "Rearranged List reverse"
    queue.printReverseList()

def test_add():
    """ Test cases
 add
    1. add into empty list
    2. add when there is single element
    3. add when there are many elements in the list
    4. check whether it returns the newly added node's reference correctly
    """
    print "Test add functionality of Queue"
    queue = Queue()
    print "Test%d:Insert into empty queue"%(1)
    nd1 = queue.add(1, 10)
    print "Queue:"
    queue.printList()
    print "Reverse Queue:"
    queue.printReverseList()
    print "Test%d:Insert with single elements"%(2)
    nd2 = queue.add(2,20)
    print "Queue:"
    queue.printList()
    print "Reverse Queue:"
    queue.printReverseList()
    print "Test%d:Inserting multiple elements in the queue"%(3)
    nd3 = queue.add(3,30)
    queue.add(4,40)
    queue.add(5,50)
    print "Queue:"
    queue.printList()
    print "Reverse Queue:"
    queue.printReverseList()
    print "Test%d:Check returned reference of the node"%(4)
    print "Queue:"
    queue.printList()
    print "Node: ", nd3.get()
    print "Node Prev:", nd3._prev.get()
    print "Node Next:", nd3._next.get()

def test_remove():
    """
    Remove 
    1. Remove on empty list
    2. Remove from single node / first and last points to the same node
    3. Remove from multiple nodes
    """
    print "Test Remove Starts"
    queue = Queue()
    print "Test%d: Remove from empty list"%(1)
    print "Original Queue:"
    queue.printList()
    data = queue.remove()
    print "Removed Node:", data
    print "Test%d: Remove node from single element queue"%(2)
    queue.add(1, 10)
    print "Original Queue:"
    queue.printList()
    data = queue.remove()
    print "Removed Node:", data
    print "Altered Queue:"
    queue.printList()
    print "Altered Reverse Queue:"
    queue.printReverseList()
    print "Test%d: Remove element from 2 node queue"%(3)
    queue.add(1, 10)
    queue.add(2, 20)
    print "Original Queue:"
    queue.printList()
    data = queue.remove()
    print "Removed node:", data
    print "Queue head and tail points the same element?", (queue.first == queue.last)
    print "Altered Queue:"
    queue.printList()
    print "Altered Reverse Queue:"
    queue.printReverseList()
    print "Test%d: Remove from multi node queue"%(4)
    queue.add(2, 20)
    queue.add(3, 30)
    queue.add(4, 40)
    print "Original List:"
    queue.printList()
    data = queue.remove()
    print "Removed Node:", data
    print "Altered Queue:"
    queue.printList()
    print "Altered Reverse Queue:"
    queue.printReverseList()
    data = queue.remove()
    print "Removed Node:", data
    print "Altered Queue:"
    queue.printList()
    print "Altered Reverse Queue:"
    queue.printReverseList()

def test_access():
    """
    access
    1. access middile elements in the multi-node list check if it goes to top and rest of the list arranges correctly
    2. access first element - no change
    3. when passed node is null
    4. when passed node do not belong to the list
    5. access last element
   """
    print "Test access Starts"
    queue = Queue()
    print "Test%d:Access first element"%(1)
    nd1 = queue.add(1, 10)
    print "Original List:"
    queue.printList()
    queue.access(nd1)
    print "Altered Queue:"
    queue.printList()
    print "Altered Reverse Queue:"
    queue.printReverseList()
    print "Test%d:Access last element"%(2)
    nd2 = queue.add(2, 20)
    nd3 = queue.add(3, 30)
    nd4 = queue.add(4, 40)
    nd5 = queue.add(5, 50)
    print "Original queue:"
    queue.printList()
    queue.access(nd5)
    print "Altered Queue:"
    queue.printList()
    print "Altered Reverse Queue:"
    queue.printReverseList()
    print "Test%d:Access 3rd element"%(3)
    print "Original Queue:"
    queue.printList()
    queue.access(nd3)
    print "Altered Queue:"
    queue.printList()
    print "Altered Reverse Queue:"
    queue.printReverseList()
    print "Test%d:pass null node"%(4)
    print "Original queue:"
    queue.printList()
    queue.access(None)
    print "Altered Queue:"
    queue.printList()
    print "Altered Reverse Queue:"
    queue.printReverseList()
    print "Test%d:pass null node"%(5)
    nd100 = QueueNode(100, 100)
    print "Original queue:"
    queue.printList()
    queue.access(nd100)
    print "Altered Queue:"
    queue.printList()
    print "Altered Reverse Queue:"
    queue.printReverseList()

        


if __name__ == "__main__":
    print "----- LruCache Testing -----"
    test_access()


