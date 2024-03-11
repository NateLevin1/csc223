# Stacks

## Section 7.1 - Introduction

-   "Pile of plates" analogy - must take top before taking others.
-   Linear, ordered data structure. Items only added or removed from the top - LIFO - last in first out.
-   Function calls are managed using a stack. A calls B, which calls C, need to be able to go back to B and then A when done - stacks work perfectly for this use case. This is called the call stack.
    -   I [implemented](https://github.com/NateLevin1/helpful-webassembly/blob/main/examples/call-stack/call-stack.wat) a call stack in WebAssembly a few years ago.
-   Stacks are frequently useful when the order of processing something matters, and when you need to be able to postpone processing of some items until later.
-   Can be implemented with either arrays or linked lists.

## Section 7.2: Array Representation of Stacks

-   `top` stores the address of the top element of the stack.
-   `max` is the maximum number of elements that can be stored in the stack.
-   `top` is null when empty, and if `top` is equal to `max`-1, the stack is full.

## Section 7.3: Operations on a Stack

-   3 basic operations: `push`, `pop`, and `peek`
    -   `push` adds an element to the top of the stack.
    -   `pop` removes the top element from the stack.
    -   `peek` returns the top element of the stack without removing it.
-   Algorithm for `push`:
    1. Check if the stack is full - `top != max-1` - fail if true (overflow).
    2. Increment `top` by 1.
    3. Store the new element in the array at `top`.
-   Algorithm for `pop`:
    1. Check if the stack is empty - `top == null` - fail if true (underflow).
    2. Store the element at `top`.
    3. Decrement `top` by 1.
    4. Return the element from step 2.
-   Algorithm for `peek`:
    1. Check if the stack is empty - `top == null` - fail if true.
    2. Return the element at `top`.

## NIST Stack Definition

> A collection of items in which only the most recently added item may be removed. The latest added item is at the top.

-   Important operations are push and pop.

### Formal Definition:

`new()`, `push(v, S)`, `top(S)`, and `popoff(S)` are defined with these axiomatic semantics, where $S$ is a stack and $v$ is a value:

-   `new()` returns a stack
-   `popoff(push(v, S))` = $S$
-   `top(push(v, S))` = $v$

`isEmpty(S)` is defined with the following axiomatic semantics:

-   `isEmpty(new())` = `true`
-   `isEmpty(push(v, S))` = `false`
