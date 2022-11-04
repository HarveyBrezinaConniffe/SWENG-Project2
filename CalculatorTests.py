from Calculator import convert_postfix, solve_postfix


# Tests for convert_postfix.
def test_convert_postfix():
    assert convert_postfix("5 - 10") == "5 10 -"
    assert convert_postfix("5 + 3 - 2") == "5 3 + 2 -"
    assert convert_postfix("10 * 2 + 3 - 6") == "10 2 * 3 + 6 -"
    assert convert_postfix("8 * exp(5.5) - 5") == "8 exp(5.5) * 5 -"
    assert convert_postfix("6 - ln(6) * 3") == "ln(6) 3 * 6 -"
    assert convert_postfix("10 - ln(6) * 5^3") == "ln(6) 5^3 * 10 -"


# Tests for solve_postfix.
def test_solve_postfix():
    assert solve_postfix("2 4 +") == 6
    assert solve_postfix("3 3 *") == 9
    assert solve_postfix("9 6 -") == 3
    assert solve_postfix("4 3 * 12 + 4 -") == 20
    assert solve_postfix(" 4 exp(4) *") == 218.393
    assert solve_postfix("ln(3) 5 +") == 6.099
    assert solve_postfix("3 5^3 *") == 375
