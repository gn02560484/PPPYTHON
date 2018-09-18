
from collections.__init__ import deque



class Node:

    def __init__(self, key, name):
        self.right: Node = None
        self.left: Node = None
        self.parent: Node = None
        self.key = key
        self.name = name

class BST:
    root: Node

    def __init__(self):
        self.root = None


    def addnode(self, key, name):
        if self.root is None:
            self.root = Node(key, name)
        else:
            self.__addNode(self.root, key, name)


    def __addNode(self, node: Node, key, name):
        if(key > node.key):
            if(node.right != None):
                self.__addNode(node.right, key, name)
            else:
                node.right = Node(key, name)
                node.right.parent = node
        elif(key < node.key):
            if(node.left != None):
                self.__addNode(node.left, key, name)
            else:
                node.left = Node(key, name)
                node.left.parent = node
        else:
            if(key == node.key):
                print("key already exist!!!!!!!!!!!!!!!!")



    def levelorderTravel(self):
        nodelist: deque[Node] = deque()
        current = self.root
        if self.root is None:
            print("There is no data in tree!!!!!!")
        else:
            while current != None:
                print(current.key," : ", current.name)
                if current.left != None:
                    nodelist.append(current.left)
                if current.right != None:
                    nodelist.append(current.right)
                try:
                    current = nodelist.popleft()
                except:
                    current = None

    def mostleft(self, node: Node):
        current = node
        while current.left != None:
            current = current.left
        return current


    def in_order_success(self, node: Node):
        current = node
        if node.right != None:
            return self.mostleft(node.right)
        else:
            if current.parent != None:
                while (current.parent != None)and(current.parent.left.key != current.key):
                    current = current.parent
                return current.parent
            else:
                return None

    def in_order_travel(self):
        current = self.mostleft(self.root)
        while current != None:
            print(current.key," : ",current.name)
            current = self.in_order_success(current)


    def search_node(self, key: int):
        current = self.root
        while (current != None)and(current.key != key):
            if key > current.key:
                current = current.right
            else:
                current = current.left
        if current is None:
            print("Key non-exist!!!!")
        return current

    def del_node(self, key: int):
        delnode = self.search_node(key)
        if delnode is None:
            return None
        childcount = 0
        if (delnode.left != None)and(delnode.right != None):  #將有兩個child的delnode和successor對調
            temp = self.in_order_success(delnode)             #successor只會有一個child 對調後delnode就會只剩一個child
            delnode.key = temp.key                             #處理完後 delnode只會有一個child
            delnode.name = temp.name
            delnode = temp
        if delnode.left != None: childcount += 1     #計算child數量
        if delnode.right != None: childcount += 1
        if childcount == 0:     #child數量為0 直接將delnode拿掉即可
            if delnode.key > delnode.parent.key:
                delnode.parent.right = None
            else:
                delnode.parent.left = None
            delnode.parent = None
        elif childcount == 1: #child數量為1
            if delnode.left != None:  #左小孩
                delnode.left.parent = delnode.parent  #將左小孩往上接parent
                if delnode.key < delnode.parent.key:    #將parent 往下接
                    delnode.parent.left = delnode.left
                else:
                    delnode.parent.right = delnode.left
            else:
                delnode.right.parent = delnode.parent  #將右小孩往上接parent
                if delnode.key < delnode.parent.key:    #將parent 往下接
                    delnode.parent.left = delnode.right
                else:
                    delnode.parent.right = delnode.right


    def right_rotation(self,node: Node):
        x = node
        y = x.right
        x.right = y.left, y.left.parent = x  #y left 接上x right
        y.parent = x.parent             #y parent接上 x parent
        if x.parent.left == x:          #x parent 接回y
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x, x.parent = y