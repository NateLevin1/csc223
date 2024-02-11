# Linked Lists

-   Useful b/c no max size and allows non-contiguous memory allocation
-   Linear collection of nodes
-   Each node has a value and a pointer to the next node
-   Last node points to null
-   "Self referential data type" b/c nodes refer to other nodes
-   Start pointer points to the first node
-   You can traverse the entire list from start pointer by following the next pointers
-   If start == null, list is empty
-   Node represented by:

```c
struct node {
    int data;
    struct node *next;
};
```

-   Nodes of a linked list don't need to be in consecutive memory locations

## Linked Lists vs Arrays

-   Both linear collections of data elements
-   LLs don't store in consecutive locations
-   LLs don't allow random access, only sequential
-   Insertions in LLs is O(1) given a node
-   LLs have unlimited capacity

## Singly Linked Lists

-   Simplest type of linked list
-   Each has a pointer to the next node, can only be traversed sequentially
-   Traversing/searching involves just continually following the next pointers
-   Insertion = setting the next pointer of the new node to the next pointer of the node before it, and setting the next pointer of the node before it to the new node
-   Insertion at beginning is faster because no traversing needed - just set start to new node, next of new node to old start
-   Deletion = setting the next pointer of the node before the one to be deleted to the next pointer of the one to be deleted, and freeing the deleted node
    -   Could underflow if start == null
    -   To delete the first node, set start to the next node and free the first node
    -   To delete last node, just set 2nd to last item's `next` to null and free the last item
