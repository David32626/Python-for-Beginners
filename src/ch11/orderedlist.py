class Node:
    def __init__(self,initdata):
        self._node_data = initdata
        self._node_next = None

    @property
    def node_data(self):
        return self._node_data
    
    @node_data.setter
    def node_data(self, new_data):
        self._node_data = new_data

    @property
    def node_next(self):
        return self._node_next

    @node_next.setter
    def node_next(self, new_next):
        self._node_next = new_next
    

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.node_data == item:
                found = True
            else:
                if current.node_data > item:
                    stop = True
                else:
                    current = current.node_next

        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.node_data > item:
                stop = True
            else:
                previous = current
                current = current.node_next

        temp = Node(item)
        if previous == None:
            temp.node_next =  self.head
            self.head = temp
        else:
            temp.node_next = current
            previous.node_next = temp

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.node_next

        return count

    def find_list_item(self):
        item_list = []
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            item_list.append(current.node_data)
            current = current.node_next
            
        return item_list

'''
mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

#print (mylist.size())
#print (mylist.search(93))
#print (mylist.search(100))
'''
