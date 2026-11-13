# Assessment 3.3 - Binary Tree with BFS and DFS (dynamic: works for any last name)
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def make_labels(name):
    """Label repeated letters so they can be told apart (M, M -> M1, M2)."""
    labels, seen = [], {}
    for ch in name:
        seen[ch] = seen.get(ch, 0) + 1
    used = {}
    for ch in name:
        if seen[ch] > 1:
            used[ch] = used.get(ch, 0) + 1
            labels.append(f"{ch}{used[ch]}")
        else:
            labels.append(ch)
    return labels


def build_tree(labels):
    """Fill the tree level by level: children of i are 2i+1 and 2i+2."""
    nodes = [Node(label) for label in labels]
    n = len(nodes)
    for i in range(n):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0] if nodes else None


def bfs(root):
    """Level-order traversal using a queue."""
    order = []
    if root is None:
        return order
    q = deque([root])
    while q:
        node = q.popleft()
        order.append(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return order


def preorder(node, order):      # Root, Left, Right
    if node is None:
        return
    order.append(node.data)
    preorder(node.left, order)
    preorder(node.right, order)


def inorder(node, order):       # Left, Root, Right
    if node is None:
        return
    inorder(node.left, order)
    order.append(node.data)
    inorder(node.right, order)


def postorder(node, order):     # Left, Right, Root
    if node is None:
        return
    postorder(node.left, order)
    postorder(node.right, order)
    order.append(node.data)


def print_tree(node, prefix="", is_left=True, is_root=True):
    """Simple sideways picture of the tree (root on the left)."""
    if node is None:
        return
    print_tree(node.right, prefix + ("" if is_root else ("│   " if is_left else "    ")), False, False)
    connector = "" if is_root else ("└── " if is_left else "┌── ")
    print(prefix + connector + node.data)
    print_tree(node.left, prefix + ("" if is_root else ("    " if is_left else "│   ")), True, False)


def main():
    name = input("Enter last name (press Enter for MANGUMPIT): ").strip().upper() or "MANGUMPIT"
    labels = make_labels(name)
    root = build_tree(labels)

    print("\nLetters (level by level):", ", ".join(labels))
    print("\nTree (sideways: right branch on top, left branch at the bottom):")
    print_tree(root)

    print("\n--- BFS (Level-order, uses a queue) ---")
    print(", ".join(bfs(root)))

    print("\n--- DFS (uses a stack / recursion) ---")
    out = []; preorder(root, out);  print("Preorder  (Root, Left, Right):", ", ".join(out))
    out = []; inorder(root, out);   print("Inorder   (Left, Root, Right):", ", ".join(out))
    out = []; postorder(root, out); print("Postorder (Left, Right, Root):", ", ".join(out))


if __name__ == "__main__":
    main()
