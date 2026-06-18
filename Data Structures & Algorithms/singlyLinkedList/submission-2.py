class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        curr = self.head
        idx = 0
        if index == 0:
            return curr[0]
        while curr[1] is not None:
            curr = curr[1]
            idx += 1
            if idx == index:
                return curr[0]
        return -1

    def insertHead(self, val: int) -> None:
        head = [val, self.head]
        self.head = head
        if self.tail is None:
            self.tail = self.head

    def insertTail(self, val: int) -> None:
        tail = [val, None]
        if self.head is None:
            self.head = tail
            self.tail = tail
        else:
            self.tail[1] = tail
            self.tail = tail

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        curr = self.head
        idx = 0
        if index == 0:
            self.head = self.head[1]
            return True
        while curr[1] is not None:
            prev = curr
            curr = curr[1]
            idx += 1
            if idx == index:
                prev[1] = curr[1]
                curr[1] = None
                if prev[1] is None:
                    self.tail = prev
                return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head
        if curr is None:
            return []
        vals = [curr[0]]
        while curr[1] is not None:
            curr = curr[1]
            vals.append(curr[0])
        return vals
        
