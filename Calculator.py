from collections import deque
import math

precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": -1, ")": -1}

# Converts an infix expression to a postfix expression
def convertToPostfix(infix):
	output = ""
	stack = deque()
	# Remove whitespace
	infix = infix.replace(" ", "")
	for char in infix:
		if char.isdigit() or char == ".":
			output += char
		elif char == "(":
			stack.append(char)
		elif char == ")":
			while stack[len(stack)-1] != "(":
				output += " "
				output += stack.pop()
			stack.pop()
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
			arg2 = argumentStack.pop()
			arg1 = argumentStack.pop()
			result = float(arg1) + float(arg2)
			argumentStack.append(str(result))
		elif symbol == "-":
			arg2 = argumentStack.pop()
			arg1 = argumentStack.pop()
			result = float(arg1) - float(arg2)
			argumentStack.append(str(result))
		elif symbol == "*":
			arg2 = argumentStack.pop()
			arg1 = argumentStack.pop()
			result = float(arg1) * float(arg2)
			argumentStack.append(str(result))
		elif symbol == "/":
			arg2 = argumentStack.pop()
			arg1 = argumentStack.pop()
			if arg2 == "0":
				return "cannot divide by 0"
			result = float(arg1) / float(arg2)
			argumentStack.append(str(result))
		elif symbol == "^":
			arg2 = argumentStack.pop()
			arg1 = argumentStack.pop()
			result = float(arg1) ** float(arg2)
			argumentStack.append(str(result))
		else:
			argumentStack.append(symbol)
	return argumentStack.pop()	

# Evaulate all exp(x) in the input by finding and replacing exp(x) with the result
def evalExp(input):
	# Convert all letters to lowercase
	output = input.lower()
	while(output.find("exp(") != -1):
		string = output
		startIndex = string.find("exp(")
		endIndex = startIndex + 4
		exp = ""
		while string[endIndex] != ")":
			exp += string[endIndex]
			endIndex += 1
		output = string.replace("exp("+exp+")", str(math.exp(float(exp))))
	return output

# Evaulate all log(x) in the input by finding and replacing log(x) with the result
def evalLog(input):
	# Convert all letters to lowercase
	output = input.lower()
	while(output.find("log(") != -1):
		string = output
		startIndex = string.find("log(")
		endIndex = startIndex + 4
		log = ""
		while string[endIndex] != ")":
			log += string[endIndex]
			endIndex += 1
		s = str(math.log(float(log)))
		output = string.replace("log("+log+")", str(math.log(float(log))))
	return output

# Evaluate an infix experssion by converting it into postfix and evauating
def calculate(input):
	try:
		string = input
		string = evalExp(string)
		string = evalLog(string)
		string =  evalPostfix(convertToPostfix(string))
		string = round(float(string), 3)
		return string
	except:
		return "Input Error"
	

if __name__ == "__main__":
	infix = "3+**8"
	print (calculate(infix))