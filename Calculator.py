from collections import deque

precedence = {"+": 1, "-": 1, "*": 2}

# Converts an infix expression to a postfix expression
def convertToPostfix(infix):
	output = ""
	stack = deque()
	# Remove whitespace
	infix = infix.replace(" ", "")
	for char in infix:
		if char.isdigit():
			output += char
		else:
			output += " "
			while len(stack) > 0 and precedence[char] <= precedence[stack[-1]]:
				output = output+stack.pop()+" "
			stack.append(char)
	while stack:
		output = output+" "+stack.pop()
	return output

# Evaluates a postfix expression
def evalPostfix(postfix):
	argumentStack = deque()
	for symbol in postfix.split(" "):
		if symbol == "+":
			arg1 = argumentStack.pop()
			arg2 = argumentStack.pop()
			argumentStack.append(arg1+arg2)
		elif symbol == "-":
			arg1 = argumentStack.pop()
			arg2 = argumentStack.pop()
			argumentStack.append(arg2-arg1)
		elif symbol == "*":
			arg1 = argumentStack.pop()
			arg2 = argumentStack.pop()
			argumentStack.append(arg1*arg2)
		else:
			argumentStack.append(int(symbol))
	return argumentStack.pop()	
