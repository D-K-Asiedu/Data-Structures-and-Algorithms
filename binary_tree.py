class Node():
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    def insert(self, data):
        if data < self.data:
            if self.left_node == None:
                self.left_node = Node(data)

            else:
                self.left_node.insert(data)

        if data > self.data:
            if self.right_node == None:
                self.right_node = Node(data)

            else:
                self.right_node.insert(data)

    def in_order(self):
        if self.left_node != None:
            self.left_node.in_order()
        
        print(self.data)

        if self.right_node != None:
            self.right_node.in_order()

lists = [3, 1, 2, 5, 7]

node = Node(lists[0])
for value in lists[1:]:
    # print(value)
    node.insert(value)

node.in_order()
