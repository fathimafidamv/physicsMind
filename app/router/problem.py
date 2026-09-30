from fastapi import APIRouter , HTTPException
from app.schemas import ProblemPublic
from app.generator import generate_problem

router=APIRouter()

@router.get("/problem",response_model=ProblemPublic)
def get_problem(difficulty: int =1):
    try:
        problem=generate_problem(difficulty)
    except ValueError as e:
        raise HTTPException(
            status_code=400 , 
            detail=str(e)
        )
    return problem