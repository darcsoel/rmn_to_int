from main import RomanToInteger


def test_3_number():
    assert RomanToInteger('III').convert() == 3


def test_4_number():
    assert RomanToInteger('IV').convert() == 4


def test_5_number():
    assert RomanToInteger('V').convert() == 5


def test_7_number():
    assert RomanToInteger('VII').convert() == 7


def test_8_number():
    assert RomanToInteger('VIII').convert() == 8


def test_9_number():
    assert RomanToInteger('IX').convert() == 9


def test_27_number():
    assert RomanToInteger('XXVII').convert() == 27


def test_58_number():
    assert RomanToInteger('LVIII').convert() == 58


def test_90_number():
    assert RomanToInteger('XC').convert() == 90


def test_94_number():
    assert RomanToInteger('XCIV').convert() == 94


def test_1994_number():
    assert RomanToInteger('MCMXCIV').convert() == 1994
