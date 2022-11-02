from Calculator import convertToPostfix, evalPostfix

# Tests for convertToPostfix.
def testConvertToPostfix():
	assert convertToPostfix("5 - 10") == "5 10 -"
	assert convertToPostfix("5 + 3 - 2") == "5 3 + 2 -"
	assert convertToPostfix("10 * 2 + 3 - 6") == "10 2 * 3 + 6 -"

# Tests for evalPostfix.
def testEvalPostfix():
	assert evalPostfix("2 4 +") == 6
	assert evalPostfix("3 3 *") == 9
	assert evalPostfix("9 6 -") == 3
	assert evalPostfix("4 3 * 12 + 4 -") == 20
