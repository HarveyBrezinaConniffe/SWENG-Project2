from Calculator import convertToPostfix, evalPostfix, evalExp, evalLog

#adding more tests for power, exponent and log

# Tests for convert_postfix.
def test_convert_postfix():
    assert convertToPostfix("5 - 10") == "5 10 -"
    assert convertToPostfix("5 + 3 - 2") == "5 3 + 2 -"
    assert convertToPostfix("10 * 2 + 3 - 6") == "10 2 * 3 + 6 -"


# Tests for solve_postfix.
def test_solve_postfix():
    assert evalPostfix("2 4 +") == "6.0"
    assert evalPostfix("3 3 *") == "9.0"
    assert evalPostfix("9 6 -") == "3.0"
    assert evalPostfix("4 3 * 12 + 4 -") == "20.0"
    assert evalPostfix("10 5 /") == "2.0"
    assert evalPostfix("10 5 /") == "2.0"
    assert evalPostfix("8 0 /") == "cannot divide by 0"
    assert evalPostfix("5 4 ^") == "625.0"
    assert evalPostfix("3 5 3 ^ *") == "375.0"

def test_eval_exp():
    assert evalExp("exp(4)") == "54.598150033144236"

def test_eval_log():
    assert evalLog("log(3)") == "1.0986122886681098"
    
