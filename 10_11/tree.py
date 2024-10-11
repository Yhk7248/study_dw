class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):        # string 으로 출력될 때 format 결정.
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


class Tree:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return repr(self.root)


if __name__ == "__main__":
    root_node = TreeNode('Root')
    child_node_1 = TreeNode('Child 1')
    child_node_2 = TreeNode('Child 2')

    child_node_1.add_child(TreeNode('Child 1.1'))
    child_node_2.add_child(TreeNode('Child 1.2'))

    child_node_2.add_child(TreeNode('Child 2.1'))

    root_node.add_child(child_node_1)
    root_node.add_child(child_node_2)

    tree = Tree(root_node)
    print(tree)
