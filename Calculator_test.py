from Calculator import convertToPostfix, evalPostfix, evalExp, evalLog, calculate

#adding more tests for power, exponent and log

#most recent push (5/11 by James)
# added more tests for each function and added tests for calculate function
# all tests pass successfully

# Tests for convert_postfix.
def test_convert_postfix():
    assert convertToPostfix("5 - 10") == "5 10 -"
    assert convertToPostfix("5 + 3 - 2") == "5 3 + 2 -"
    assert convertToPostfix("10 * 2 + 3 - 6") == "10 2 * 3 + 6 -"
    assert convertToPostfix("5 / 2 * 8") == "5 2 / 8 *"
    assert convertToPostfix("5^5 + 7") == "5 5 ^ 7 +"
    assert convertToPostfix("7 + (5 + 2)") == "7 5 2 + +"
    assert convertToPostfix("(5 / 2) - 8") == "5 2 / 8 -"
    assert convertToPostfix("(4 * 7) - 9^4") == "4 7 * 9 4 ^ -"
    


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
    assert evalPostfix("4 7 * 9 4 ^ -") == "-6533.0"
    

def test_eval_exp():
    assert evalExp("exp(4)") == "54.598150033144236"
    assert evalExp("exp(7.9)") == "2697.28232826851"
    assert evalExp("exp(-3)") == "0.049787068367863944"

def test_eval_log():
    assert evalLog("log(3)") == "1.0986122886681098"
    assert evalLog("log(6.5)") == "1.8718021769015913"

def test_calculate():
    assert calculate("3+5*exp(4.2)/(5+7)") == "30.786"
    assert calculate("3+**8") == "Error"
    assert calculate("exp(4)") == "54.598"
    assert calculate("8 * 8 / 16") == "4"
    assert calculate("7 * (4 + 1) - 7 * 2") == "21"
    assert calculate("18 + 5 / 0") == "cannot divide by 0"
    assert calculate("(8*2)-3^2+(5*2)") == "17"
    
