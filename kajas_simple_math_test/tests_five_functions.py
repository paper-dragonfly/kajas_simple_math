from five_functions import kaja_plus, kaja_mult, kaja_div, kaja_multimult, kaja_wordsum

tval1 = 0
tval2 = 2
tval3 = -2
tval4 = "az"

def test_kajas_five_functions():
    assert kaja_plus(tval1) == 26
    assert kaja_plus(tval2) == 28
    assert kaja_plus(tval3) == 24
    assert kaja_plus("word") == "non-num input"
    # assert kaja_plus(tval4) == ?
    print("kaja_plus test successful")

    assert kaja_mult(tval1) == 0
    assert kaja_mult(tval2) == 52
    assert kaja_mult(tval3) == -52
    print("kaja_mult test successful")

    assert kaja_div(tval1) == 0
    assert kaja_div(tval2) == tval2/26
    assert kaja_div(tval3) == tval3/26
    print("kaja_div test successful")

    assert kaja_multimult(tval1, tval2, tval3) == 0
    assert kaja_multimult((tval1+1), tval2, tval3) == -4
    assert kaja_multimult(tval1+1, tval2*-1, tval3) == 4
    print("kaja_multimult successful")

    assert kaja_wordsum("a") == 1
    assert kaja_wordsum("z") == 26
    assert kaja_wordsum("ya z") == 52

    print("ALL TESTS GOOD")
    return 

test_kajas_five_functions() 



