from Calculator import convertToPostfix, evalPostfix, evalExp, evalLog

#adding more tests for power, exponent and log

# Tests for convert_postfix.
def test_convert_postfix():
    assert convertToPostfix("5 - 10") == "5 10 -"
    assert convertToPostfix("5 + 3 - 2") == "5 3 + 2 -"
    assert convertToPostfix("10 * 2 + 3 - 6") == "10 2 * 3 + 6 -"
    assert convertToPostfix("8 * exp(5.5) - 5 / 2") == "8 exp(5.5) * 5 2 / -"
    assert convertToPostfix("6 - log(6) * 3") == "log(6) 3 * 6 -"
    assert convertToPostfix("10 - log(6) * 5^3") == "log(6) 5^3 * 10 -"


# Tests for solve_postfix.
def test_solve_postfix():
    assert evalPostfix("2 4 +") == 6
    assert evalPostfix("3 3 *") == 9
    assert evalPostfix("9 6 -") == 3
    assert evalPostfix("4 3 * 12 + 4 -") == 20
    assert evalPostfix("10 5 /") == 2
    assert evalPostfix("10 5 /") == 2
    assert evalPostfix("8 0 /") == "cannot divide by 0"
    assert evalPostfix("5^4") == 625
    assert evalPostfix("3 5^3 *") == 375

def test_eval_exp():
    assert evalExp(" 4 exp(4) *") == 218.393

def test_eval_log():
    assert evalLog("log(3) 5 +") == 6.099
    
