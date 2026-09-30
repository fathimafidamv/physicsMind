from app.checker import check_answer


def test_exact_answer_is_correct():
    assert check_answer(35.5,35.5)

def test_wrong_answer_is_rejected():
    assert not check_answer(40, 35.35)

def  test_rounded_answer_is_correct():
    assert check_answer(35.35,35.4)