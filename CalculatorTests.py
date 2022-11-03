from Calculator import convert_postfix, solve_postfix


# Tests for convert_postfix.
def test_convert_postfix():
    assert convert_postfix("5 - 10") == "5 10 -"
    assert convert_postfix("5 + 3 - 2") == "5 3 + 2 -"
    assert convert_postfix("10 * 2 + 3 - 6") == "10 2 * 3 + 6 -"


# Tests for solve_postfix.
def test_solve_postfix():
    assert solve_postfix("2 4 +") == 6
    assert solve_postfix("3 3 *") == 9
    assert solve_postfix("9 6 -") == 3
    assert solve_postfix("4 3 * 12 + 4 -") == 20
