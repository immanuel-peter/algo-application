from stack import IntStack

def run_tests():
    stack = IntStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.peek() == 30, f"Expected top of stack to be 30, got {stack.peek()}"

    assert stack.pop() == 30, "Expected to pop 30"
    assert stack.peek() == 20, f"Expected top of stack to be 20, got {stack.peek()}"
    assert stack.pop() == 20, "Expected to pop 20"
    assert stack.pop() == 10, "Expected to pop 10"
    try:
        stack.pop()
    except IndexError:
        print("Expected IndexError on empty stack pop")
    else:
        raise AssertionError("Expected IndexError on empty stack pop")

    stack.push(100)
    assert stack.peek() == 100, f"Expected top of stack to be 100, got {stack.peek()}"
    stack.push(200)
    assert stack.peek() == 200, f"Expected top of stack to be 200, got {stack.peek()}"
    stack.pop()
    assert stack.peek() == 100, f"Expected top of stack to be 100 after pop, got {stack.peek()}"
    try:
        empty_stack = IntStack()
        empty_stack.peek()
    except IndexError:
        print("Expected IndexError on empty stack peek")
    else:
        raise AssertionError("Expected IndexError on empty stack peek")

    stack = IntStack()
    assert stack.size() == 0, f"Expected size 0, got {stack.size()}"
    stack.push(10)
    assert stack.size() == 1, f"Expected size 1, got {stack.size()}"
    stack.push(20)
    assert stack.size() == 2, f"Expected size 2, got {stack.size()}"
    stack.pop()
    assert stack.size() == 1, f"Expected size 1 after pop, got {stack.size()}"

    print("All tests passed!")

run_tests()
# Output:
# Caught expected IndexError on pop from empty stack
# Caught expected IndexError on peek from empty stack
# All tests passed!
