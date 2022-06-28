import gc


class DoublyLinkedList:

    def __init__(self,data, next=None, prev=None):
        self.data = data
        self.prev = None
        self.next = None



class FirstNonRepeating:

    def __init__(self):
        self.indll=[None for i in range(26)]
        self.repeatarr=[False for i in range(26)]
        self.head = None


    def appendnode(self,ch):
        node = DoublyLinkedList(ch)
        if self.head is None:
            self.head = node
            return node
        else:
            last = self.head
            while last.next:
                last=last.next
            last.next = node
            node.prev = last
            return node


    def removenode(self,node):
        if self.head == node:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next

        gc.collect()
    def findfirstnonrepeating(self,ch):
        pos = ord(ch)-ord('a')
        if self.repeatarr[pos] is False:
            if self.indll[pos] is None:
                self.indll[pos] = self.appendnode(ch)
            else:
                self.removenode(self.indll[pos])
                self.repeatarr[pos]=True
            return -1 if self.head is None else self.head.data
        else:
            return -1







m = FirstNonRepeating()
print(m.findfirstnonrepeating("g"))
print(m.findfirstnonrepeating("e"))
print(m.findfirstnonrepeating("e"))
print(m.findfirstnonrepeating("k"))
print(m.findfirstnonrepeating("g"))


