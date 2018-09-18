from test.BST import BST

tree = BST()
tree.addnode(8, "龜仙人")
tree.addnode(1000,"悟空")
tree.addnode(2,"克林")
tree.addnode(513,"比克")

tree.levelorderTravel()
print("-----------------------")
# temp = tree.in_order_success(tree.root)
#
# print(temp.key,":",temp.name)

# tree.in_order_travel()

# print(tree.search_node(7).name)
tree.in_order_travel()
print("-------------after del 8--------------")
tree.del_node(7)
tree.levelorderTravel()
print("-----in order---------------")
tree.in_order_travel()