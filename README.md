## Question 2: Implement Stack (Python)

The task was to implement an integer stack without using container structures (e.g., lists, vectors). The stack was also to have a push, pop, peek, and size method.

First of all, the term stack should be defined. A stack is a structure that follows a last-in/first-out (LIFO) pattern, meaning when a new element is pushed to the stack, that element will also be the first to be popped from the stack when invoked.

My choice of language was Python, and I decided to implement a linked list to implement the stack given the constraints. My initial thought process was to ensure there was a node that pointed to top of the stack so that push, pop, and peek operations could happen in an efficient manner. The size operation could employ a count variable that simply keeps track of the size of the linked list during each push and pop operation.

First, I implemented a `Node` class which would construct the linked list in the integer stack. The `Node` object takes in a parameter `value`, allowing it to store the integer. It also contains an instance variable `next` which provides a pointer to the next node in the linked list.

Then, I implemented the `IntStack` class. It contains two instance variables `top` and `count`. The `top` variable allows the `IntStack` object to keep track of the top of the stack in an efficient manner, as will be shown in some of the operations below. The `count` variable allows for easy tracking of the size of the stack as it shrinks and grows.
- `.push(value)` (Adds element to top of stack)
  - Takes in a parameter `value`, which is the new integer to be added to the top of the stack
  - `new_node.next` is assigned to the current `self.top`, linking the new node to the previous top of the stack
  - `self.top` is updated to reference `new_node`, restablishing the top of the stack
    - The two previous steps are important because they ensures the correct order of the stack
  - `self.count` is incremented by 1
- `.pop()` (Removes top element from stack and returns it)
  - Checks if the stack is empty (`self.top is None`)
    - If true, raises an error stating that the operation cannot happen
  - Retrieves current `self.top.value` and stores it in `value` because `self.top.value` will change
  - Updates top of the stack by assigning `self.top` to `self.top.next`
  - `self.count` is decremented by 1
  - Returns `value` and stack is now updated
- `.peek()` (Returns current integer on top of the stack)
  - Checks if the stack is empty (`self.top is None`)
    - If true, raises an error stating that the operation cannot happen
  - Returns `self.top.value` without changing the stack
- `.size()` (Returns amount of integers in the stack)
  - Returns `self.count`
 
All operations in the `IntStack` class happen in O(1) or constant time, so it is maximally efficient.
