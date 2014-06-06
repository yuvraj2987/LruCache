

from queue import Queue

class LruCache:

    def __init__(self, size):
        self.size = size
        self.hash_map = {}
        self.queue    = Queue()


    def add(self, key, value):
        """
        add key and value in hash_map and queue
        """
        hash_map = self.hash_map
        queue = self.queue

        
        #Remove element from the cache if size is full
        if (len(hash_map) >= self.size):
            remove_node_list = queue.remove()
            del hash_map[remove_node_list[0]]

        #Add element in cache
        node = queue.add(key, value)
        hash_map[key] = node


    def find(self, key):
        """ searches for key in cache
            if found moves the cache node to the head of the queue
            and returns the value
            returns None if not found
        """
        hash_map = self.hash_map
        queue    = self.queue

        node = hash_map.get(key)

        if node is None:
            return None
        
        queue.access(node)
        return node.get()[1]


#Class LruCache ends

def test():
    cache = LruCache(3)
    cache.add(1, 10)
    cache.add(2, 20)
    cache.add(3, 30)
    print "Test%d:find existing entry in the cache"%(1)
    val = cache.find(2)
    print "Value returned by cache:", val
    print "Test%d:find non existing entry in the cache"%(2)
    val = cache.find(100)
    print "Value returned by cache:", val
    print "Test%d:check if last entry gets overwritten"%(3)
    cache.find(3)
    cache.add(4, 40)
    val1 = cache.find(1)
    val2 = cache.find(4)
    print "Value returned for key1:", val1
    print "Value retyurned for key4:", val2



if __name__ == "__main__":
    print "Lru Cache Test"
    test() 

