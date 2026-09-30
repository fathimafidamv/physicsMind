from fastapi import APIRouter , HTTPException
from app.schemas import ProblemPublic , AnswerChecker ,Problem
from app.generator import generate_problem
from app.checker import check_answer

router=APIRouter()


PROBLEMS: dict[int, Problem] = {}
QUANTITIES = ("time_of_flight", "max_height", "range")


@router.get("/problem",response_model=ProblemPublic)
def get_problem(difficulty: int =1):
    try:
        problem=generate_problem(difficulty)
        PROBLEMS[problem.id] = problem
    except ValueError as e:
        raise HTTPException(
            status_code=400 , 
            detail=str(e)
        )
    return problem


@router.post("/check")
def answer(submission:AnswerChecker , problem_id: int):
    problem = PROBLEMS.get(problem_id)
    if problem is None:
        raise HTTPException(
            status_code=400,
            detail="Problem not found"
        )

    if submission.quantity not in QUANTITIES:
        raise HTTPException(
            status_code=400,
            detail="Quantity not found"
        )
    correct_value = getattr(problem.solution,submission.quantity)
    is_correct= check_answer(submission.value , correct_value )
    return {
        "correct":is_correct
    }