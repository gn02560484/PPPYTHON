# from test.BST import BST
from test.RBT import RBT, Node

tree = RBT()
tree.addnode(50, "50")
tree.addnode(20,"20")
tree.addnode(70,"70")
tree.addnode(10,"10")
tree.addnode(40,"40")
tree.addnode(60,"60")
tree.addnode(80,"80")
tree.addnode(30,"30")
tree.addnode(75,"75")
tree.addnode(25,"25")
tree.addnode(79,"79")

tree.levelorderTravel()
print("-------------level order----------")

tree.in_order_travel()
print("---------------in order-------------------------------------")



# print(tree.root.right.left.right.name)
# print(tree.root.right.left.left.name)
# print("-------------after--------------")
# tree.levelorderTravel()
# print("-----in order---------------")
# tree.in_order_travel()

