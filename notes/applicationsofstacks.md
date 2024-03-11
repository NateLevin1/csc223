# 7.7: Applications of Stacks

## Reversing a list

**Summary**: Reverse the order of a list of items.

**Implementation Reqs**: Push each item onto the stack, then pop each item off the stack.

## Parentheses checker

**Summary**: Check if a string of parentheses is valid - e.g. `({})` but not `({)`.

**Implementation Reqs**: Push opening parentheses onto the stack, then pop each closing parentheses off the stack. If the stack is empty at the end and popping always resulted in the correct value, the string is valid.

## Conversion of an infix expression into a postfix expression

**Summary**: Postfix expression = operator placed after the operands. Infix expression = operator placed between the operands. E.g. `A + B` becomes `A B +`.

**Implementation Reqs**: Use a stack to store operators and parentheses. Iterate, pushing operators onto the stack when needed, and inserting operands directly into the output.

## Evaluation of a postfix expression

**Summary**: Much easier than evaluating infix notation. Finds the value of the postfix expression.

**Implementation Reqs**: Push operands onto the stack. When an operator is found, pop 2 off the stack and perform the operation, then push the result back onto the stack.

## Conversion of an infix expression into a prefix expression

**Summary**: Prefix expression = operator placed before the operands. Infix expression = operator placed between the operands. `A + B` becomes `+ A B`. Like the reverse of converting to postfix.

**Implementation Reqs**: Either: reverse the string (keeping parentheses balanced), then convert to postfix, then reverse again, or utilize an operator and operand stack, popping and pushing values accordingly.

## Evaluation of a prefix expression

**Summary**: Gets the value of an expression written in prefix notation.

**Implementation Reqs**: Loop over the string in reverse. Push operands to the operand stack, when encountering an operator, pop the top 2 operands, perform the operation, and push the result back onto the stack.

## Recursion

**Summary**: Functions that call themselves to solve a problem. Common problems with simple recursive solutions: factorial, GCD, exponent value, fibonacci.

**Direct Recursion**: Function explicitly calls itself.
**Indirect Recursion**: Contains a call to a function that calls the original function.
**Tail Recursion**: The recursive call is the last thing the function does - no operations pending. Non-tail recursion can be converted to tail recursion by passing the result of the recursive call as an argument to the function, called an auxiliary parameter.

Linear vs tree recursion - tail = linear, non-tail = tree.

## Tower of Hanoi

**Summary**: Classic recursive problem, because if can solve $n-1$ case, can solve $n$-th case. Move rings between pegs without changing order, using a spare peg.

**Implementation Reqs**: Base case: if $n=1$, move a ring from A to C using B as spare. Recursive case:
move $n-1$ rings from A to B using C as spare, then move the one ring left in A to C using B as spare, then move $n-1$ rings from B to C using A as spare.

### Recursion vs Iteration

Advantages of recursion:

-   Code can be shorter and simpler.
-   Follows a divide and conquer technique.

Disadvantages of recursion:

-   Extra overhead in function calls
-   Difficult concept
-   Requires system stack space
-   Takes more resources
-   Aborting a recursive function can be difficult
-   Difficult to find algorithm bugs
