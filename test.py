from typing import Any

class Node:
    def __init__(self, val: Any):
        self.val = val
        self.children = []

    def adopt(self, *val_list: list[Any]):
        for val in val_list:
            self.children.append(Node(val))

    def __getitem__(self, index: int) -> "Node":
        return self.children[index]
    
root = Node("root")
root.adopt("apple", "orange", "pear", "pineapple")
root[0].adopt("banana", "durian")
root[1].adopt("juice")
root[1][0].adopt("juice2")
root[1][0][0].adopt("potato", "soup")
root[2].adopt("kiwi", "avocado")
root[2][1].adopt("cherry tomato", "soup")


from src.pprint_tree import pprint_tree

pprint_tree(root)

"""
          _____________________________________root________________________________
          |                       |                   |                           |
   _____apple______             orange          _____pear_______________     pineapple
   |              |               |             |                      |
banana         durian           juice         kiwi          ________avocado__________
                                  |                         |                       |
                          _____juice2______          cherry tomato                soup
                          |               |
                       potato           soup

"""
