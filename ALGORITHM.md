# Assessment 3.6: Algorithm - DFS Methods in Tree

**Tree:** last name **MANGUMPIT**, letters placed level by level, left to right (the two M's are labeled M1 and M2).

```
              M1
           /      \
          A         N
         / \       / \
        G   U    M2   P
       / \
      I   T
```

## A. Build the Tree
1. START
2. Read the last name (default `MANGUMPIT`).
3. Label repeated letters (M, M -> M1, M2) and create one node per letter.
4. For each node at index `i` (starting at 0):
   - Left child = node at index `2i + 1` (if it exists)
   - Right child = node at index `2i + 2` (if it exists)
5. The node at index 0 is the **root**.

## B. PreOrder (Root -> Left -> Right)
```
PREORDER(node)
1. If node is NULL, return
2. Visit node (add its data to the list)
3. PREORDER(node.left)
4. PREORDER(node.right)
```

## C. InOrder (Left -> Root -> Right)
```
INORDER(node)
1. If node is NULL, return
2. INORDER(node.left)
3. Visit node (add its data to the list)
4. INORDER(node.right)
```

## D. PostOrder (Left -> Right -> Root)
```
POSTORDER(node)
1. If node is NULL, return
2. POSTORDER(node.left)
3. POSTORDER(node.right)
4. Visit node (add its data to the list)
```

## E. PreOrder using a Stack (check)
```
1. Push root onto the stack
2. While the stack is not empty:
   a. Pop a node and visit it
   b. Push its right child (if any)
   c. Push its left child (if any)
```

## F. Main Program
1. Build the tree (Part A).
2. Run PREORDER, INORDER and POSTORDER from the root, each with an empty list.
3. Display the three results.
4. END

## Expected Output
| Traversal | Result |
|---|---|
| PreOrder | M1, A, G, I, T, U, N, M2, P |
| InOrder | I, G, T, A, U, M1, M2, N, P |
| PostOrder | I, T, G, U, A, M2, P, N, M1 |
