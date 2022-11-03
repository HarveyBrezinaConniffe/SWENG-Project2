from collections import deque

Precedence = {'+': 1, '-': 1, '*': 2}  # dictionary to help check precedence


# Function that takes an infix expression and returns it in postfix form.
def convert_postfix(infix):
    output = ""
    stack = deque()
    infix = infix.replace(' ', '')
    # remove any whitespace in input string
    for c in infix:
        if c.isdigit():
            output += c
        else:
            output += " "
            while len(stack) > 0 and Precedence[c] <= Precedence[stack[-1]]:
                output = output + stack.pop() + " "
            stack.append(c)
    while stack:
        output = output + " " + stack.pop()
    return output


# Function that takes a postfix expression and returns the result.
def solve_postfix(postfix):
    argument_stack = deque()
    for symbol in postfix.split(" "):
        if symbol == "+":
            arg1 = argument_stack.pop()
            arg2 = argument_stack.pop()
            argument_stack.append(arg1 + arg2)
        elif symbol == "-":
            arg1 = argument_stack.pop()
            arg2 = argument_stack.pop()
            argument_stack.append(arg2 - arg1)
        elif symbol == "*":
            arg1 = argument_stack.pop()
            arg2 = argument_stack.pop()
            argument_stack.append(arg1 * arg2)
        else:
            argument_stack.append(int(symbol))
    return argument_stack.pop()


def calculate(eq):
    result = solve_postfix(convert_postfix(eq))
    return result
