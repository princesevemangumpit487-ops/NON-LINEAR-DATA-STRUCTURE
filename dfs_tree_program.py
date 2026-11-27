# Assessment 3.6 - DFS Methods in Tree (PreOrder, InOrder, PostOrder)
# Default: last name MANGUMPIT (the two M's are labeled M1 and M2)


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


# ---------- DFS methods (recursive) ----------
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


# ---------- DFS using an explicit stack (PreOrder) ----------
def preorder_stack(root):
    """Iterative DFS: push right first so the left child is visited first."""
    order, stack = [], [root] if root else []
    while stack:
        node = stack.pop()
        order.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def print_tree(node, level=0, label="Root"):
    """Print the tree as an indented outline (L = left child, R = right child)."""
    if node is None:
        return
    print("    " * level + f"{label}: {node.data}")
    print_tree(node.left, level + 1, "L")
    print_tree(node.right, level + 1, "R")


def main():
    name = input("Enter last name (press Enter for MANGUMPIT): ").strip().upper() or "MANGUMPIT"
    labels = make_labels(name)
    root = build_tree(labels)

    print("\nLetters (level by level):", ", ".join(labels))
    print("\nTree:")
    print_tree(root)

    print("\n--- DFS Methods in Tree ---")
    out = []; preorder(root, out);  print("PreOrder  (Root, Left, Right):", ", ".join(out))
    out = []; inorder(root, out);   print("InOrder   (Left, Root, Right):", ", ".join(out))
    out = []; postorder(root, out); print("PostOrder (Left, Right, Root):", ", ".join(out))

    print("\nPreOrder using a stack (check):", ", ".join(preorder_stack(root)))


if __name__ == "__main__":
    main()
