#builds the linked list for traversing
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.cache = {}
        #initialise the two pointers
        self.left = Node(0,0)
        self.right = Node(0,0)
        #connects the two nodes
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, Node):
        Node1 = Node.prev
        Node2 = Node.next

        Node1.next = Node2
        Node2.prev = Node1

    def insert(self, Node):
        prev = self.right.prev
        next = self.right

        Node.next = self.right
        Node.prev = prev
        prev.next = Node
        next.prev = Node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].value = value
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = Node(key, value)
                self.insert(self.cache[key])
            else:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
                new_node = Node(key, value)
                self.cache[key] = new_node
                self.insert(self.cache[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)