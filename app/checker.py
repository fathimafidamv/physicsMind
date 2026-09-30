import math


def check_answer(student_value:float , correct_value:float , rel_tol=0.01) ->bool:
    answer=math.isclose(student_value,correct_value,rel_tol=rel_tol)
    return answer
