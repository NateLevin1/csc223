# Queues

## Section 8.1 - Introduction

-   Like people waiting in lines - first person in line is first to be served.
-   First in, first out (FIFO)
-   Can be implemented with arrays or linked lists.

## Section 8.2 - Array Representation of Queues

-   `front` and `rear` pointers point to where the first and last elements are in the queue - where deletions and insertions should be performed, respectively.
-   To insert an element into an array queue:
    -   Check if the queue is full - `rear == max-1`
        -   fail if true (overflow).
    -   Otherwise, if the queue is empty, set `front` and `rear` to 0.
    -   Otherwise, increment `rear` by 1 and store the new element in the array at `rear`.
-   To delete an element from an array queue:
    -   Check if the queue is empty or if the front is greater than the rear.
        -   fail if true (underflow).
    -   Otherwise, temporarily store the element at `front`, increment `front` by 1, and return the temp var.

## Section 8.3 - Linked List Representation of Queues

-   Drawback of arrays is that they have a fixed size. Linked-list based queues can grow and shrink as needed. Time complexity is the same for both.
-   `front` and `rear` pointers point to the first and last nodes in the queue.
-   Insert operation
    -   If empty, set both `front` and `rear` to the new node.
    -   Otherwise, set the `next` pointer of the current `rear` node to the new node and update `rear` to the new node.
-   Delete operation
    -   If empty, fail (underflow).
    -   Otherwise, store the `front` node, update `front` to the `next` node, and free the stored `front` node.
