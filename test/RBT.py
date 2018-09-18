
from collections.__init__ import deque



class Node:

    def __init__(self, key: int, name: str):
        self.right: Node = None
        self.left: Node = None
        self.parent: Node = None
        self.key = key
        self.name = name
        self.color = 0    # 0:紅色  1:黑色   初始為紅色

class RBT:
    root: Node

    def __init__(self):
        self.neel = Node(None, "NIL")
        self.neel.color = 1
        self.root = None


    def addnode(self, key, name):
        if self.root is None:
            self.root = Node(key, name)
            self.root.parent = self.neel
            self.root.right = self.neel
            self.root.left = self.neel
            self.root.color = 1
        else:
            self.__addNode(self.root, key, name)


    def __addNode(self, node: Node, key, name):
        node_insert: Node
        if(key > node.key):
            if(node.right != self.neel):
                self.__addNode(node.right, key, name)
            else:
                node.right = Node(key, name)
                node_insert = node.right
                node.right.right = self.neel
                node.right.left = self.neel  #新增node的child接到neel
                node.right.parent = node
                self.insert_fixRBT(node_insert)
        elif(key < node.key):
            if(node.left != self.neel):
                self.__addNode(node.left, key, name)
            else:
                node.left = Node(key, name)
                node_insert = node.left
                node.left.right = self.neel
                node.left.left = self.neel    #新增node的child接到neel
                node.left.parent = node
                self.insert_fixRBT(node_insert)
        else:
            if(key == node.key):
                print("key already exist!!!!!!!!!!!!!!!!")




    def levelorderTravel(self):
        nodelist: deque[Node] = deque()
        current = self.root
        if self.root is None:
            print("There is no data in tree!!!!!!")
        else:
            while current != self.neel:
                print(current.key," : ", current.name," : ",current.color)
                if current.left != self.neel:
                    nodelist.append(current.left)
                if current.right != self.neel:
                    nodelist.append(current.right)
                try:
                    current = nodelist.popleft()
                except:
                    current = self.neel

    def mostleft(self, node: Node):
        current = node
        while current.left != self.neel:
            current = current.left
        return current


    def in_order_success(self, node: Node):
        current = node
        if node.right != self.neel:
            return self.mostleft(node.right)
        else:
            if current.parent != self.neel:
                while (current.parent != self.neel)and(current.parent.left.key != current.key):
                    current = current.parent
                return current.parent
            else:
                return self.neel

    def in_order_travel(self):
        current = self.mostleft(self.root)
        while current != self.neel:
            print(current.key," : ",current.name," : ",current.color)
            current = self.in_order_success(current)


    def search_node(self, key: int):
        current = self.root
        while (current != self.neel)and(current.key != key):
            if key > current.key:
                current = current.right
            else:
                current = current.left
        if current == self.neel:
            print("Key non-exist!!!!")
            return self.neel
        return current

    def del_node(self, key: int):
        delnode = self.search_node(key)
        if delnode == self.neel:
            return self.neel
        childcount = 0
        if (delnode.left != self.neel)and(delnode.right != self.neel):  #將有兩個child的delnode和successor對調
            temp = self.in_order_success(delnode)             #successor只會有一個child 對調後delnode就會只剩一個child
            delnode.key = temp.key                             #處理完後 delnode只會有一個child
            delnode.name = temp.name
            delnode = temp
        if delnode.left != self.neel: childcount += 1     #計算child數量
        if delnode.right != self.neel: childcount += 1
        if childcount == 0:     #child數量為0 直接將delnode拿掉即可
            if delnode.key > delnode.parent.key:
                delnode.parent.right = self.neel
            else:
                delnode.parent.left = self.neel
            delnode.parent = self.neel
        elif childcount == 1: #child數量為1
            if delnode.left != self.neel:  #左小孩
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


    def left_rotation(self,node: Node):
        x = node
        y = x.right
        if self.root == x:
            self.root =y
        x.right = y.left
        y.left.parent = x  #y left 接上x right
        y.parent = x.parent             #y parent接上 x parent
        if x.parent.left == x:          #x parent 接回y
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def right_rotation(self,node: Node):
        x = node
        y = x.left
        if self.root == x:
            self.root = y
        x.left = y.right
        y.right.parent = x
        y.parent = x.parent
        if x.parent.left == x:          #x parent 接回y
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y


    def insert_fixRBT(self,node: Node):
        current = node
        # current是在祖父的left tree
        if current.parent == current.parent.parent.left:
            while current.color == 0 and current.parent.color ==0:
                uncle = current.parent.parent.right
                if uncle.color ==1 and current == current.parent.right:  #case2轉乘case3
                    current = current.parent
                    self.left_rotation(current)
                if current.parent.color == 0 and uncle.color == 0:  #case1
                    current.parent.color = 1
                    uncle.color = 1
                    current.parent.parent.color = 0
                    current = current.parent.parent
                else:   #case3
                    current.parent.color = 1
                    current.parent.parent.color = 0
                    self.right_rotation(current.parent.parent)
        else:
            while current.color == 0 and current.parent.color == 0:
                uncle = current.parent.parent.left
                if uncle.color==1 and current==current.parent.left:
                    current = current.parent
                    self.right_rotation(current)
                if current.parent.color ==0 and uncle.color ==0: #case1
                    current.parent.color = 1
                    uncle.color = 1
                    current.parent.parent.color = 0
                    current = current.parent.parent
                else: #case3
                    current.parent.color = 1
                    current.parent.parent.color = 0
                    self.left_rotation(current.parent.parent)
        self.root.color = 1


