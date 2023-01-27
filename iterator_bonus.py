class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return (
            f"Node with value: {self.value}"
        )


class MeuIterator:
    def __init__(self, root):
        self.traversal = []
        self.move_left(root)

    def move_left(self, current):
        while current:
            self.traversal.append(current)
            current = current.left

    def __next__(self):
        try:
            current = self.traversal.pop()
            if current.right:
                self.move_left(current.right)
            return current
        except IndexError:
            raise StopIteration

    # def __iter__(self):
    #     return MeuIterator(self.root)


class MeuIteravel:
    def __init__(self, root):
        self.root = root

    def __iter__(self):
        return MeuIterator(self.root)


# Árvore
root = Node(5)
root.right = Node(6)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.left.right.right = Node(4)

iteravel = MeuIteravel(root)

for node in iteravel:
    print(node)
