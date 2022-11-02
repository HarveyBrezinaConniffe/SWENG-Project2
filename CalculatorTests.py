from Calculator import convertToPostfix, evalPostfix

# Tests for convertToPostfix.
def testConvertToPostfix():
	assert convertToPostfix("5 - 10") == ""

# Tests for evalPostfix.
def testEvalPostfix():
	assert evalPostfix("2 4 +") == -1
