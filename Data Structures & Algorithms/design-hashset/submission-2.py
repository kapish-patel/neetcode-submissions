class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next
    

class MyHashSet:

    def __init__(self):
        self.keys = [ListNode() for _ in range(10000)]
        

    def add(self, key: int) -> None:
        current = self.getNodeHead(key)
        while current.next:
            if current.next.data == key:
                return
            current = current.next
        current.next = ListNode(key)

    def remove(self, key: int) -> None:
        current = self.getNodeHead(key)
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
        return
        
        
    def contains(self, key: int) -> bool:
        current = self.getNodeHead(key)
        while current.next:
            if current.next.data == key:
                return True
            current = current.next
        return False
    
    def getNodeHead(self, key: int):
        return self.keys[key % 10000]




# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)