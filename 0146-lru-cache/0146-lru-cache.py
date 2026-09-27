class Node:
    def __init__(self, key, val):
        # Store both key and value because we need the key
        # when removing an LRU node from the hashmap
        self.key, self.val = key, val

        # Pointers for the doubly linked list
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        # Hashmap: key -> Node
        # Allows O(1) access to any cached node
        self.cache = {}

        # Dummy nodes representing the boundaries of the linked list
        # left.next  = Least Recently Used (LRU) node
        # right.prev = Most Recently Used (MRU) node
        self.left, self.right = Node(0, 0), Node(0, 0)

        # Initially connect the two dummy nodes
        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        # Remove node from the doubly linked list by
        # connecting its previous node directly to its next node
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev


    def insert(self, node):
        # Insert node at the right side of the list,
        # making it the Most Recently Used (MRU) node
        prev, nxt = self.right.prev, self.right

        # Connect previous MRU node -> new node
        # and right dummy <- new node
        prev.next = node
        nxt.prev = node

        # Connect new node back to its neighbours
        node.prev = prev
        node.next = nxt


    def get(self, key: int) -> int:
        if key in self.cache:
            # Accessing a key makes it the Most Recently Used,
            # so remove it from its current position...
            self.remove(self.cache[key])

            # ...and move it to the MRU position
            self.insert(self.cache[key])

            return self.cache[key].val

        # Key does not exist in the cache
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the old node from the linked list
            # because it will be replaced with a new node
            self.remove(self.cache[key])

        # Create/update the node in the hashmap
        self.cache[key] = Node(key, value)

        # Newly inserted/updated key becomes the MRU node
        self.insert(self.cache[key])

        # If capacity is exceeded, remove the Least Recently Used node
        if len(self.cache) > self.cap:
            # LRU node is always directly after the left dummy
            lru = self.left.next

            # Remove LRU node from linked list
            self.remove(lru)

            # Remove LRU node from hashmap
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)