
def is_balanced(expression):
    stack = []
    
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in expression:
        # Opening bracket: push into stack
        if char in "({[":
            stack.append(char)

        # Closing bracket: check the top of stack
        elif char in ")}]":
            if not stack:
                return False

            if stack.pop() != pairs[char]:
                return False

    # Stack should be empty if all brackets matched
    return len(stack) == 0


expression = input("Enter an expression: ")

if is_balanced(expression):
    print("Balanced")
else:
    print("Not Balanced")

