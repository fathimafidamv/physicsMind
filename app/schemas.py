from pydantic import BaseModel , Field 


class ProjectileParams(BaseModel):
    speed: float = Field(gt=0 , description="Launch speed m/s")
    angle: float = Field(gt=0 , lt=90 , description="Launch angle")
    g : float = 9.8

class ProjectileSolution(BaseModel):
    time_of_flight: float
    max_height: float
    range: float

class Problem(BaseModel):
    id: int
    topic: str
    params: ProjectileParams
    question: str
    solution: ProjectileSolution

class  ProblemPublic(BaseModel):
    id: int
    topic: str
    params: ProjectileParams
    question: str    

class AnswerChecker(BaseModel):
    problem_id: int
    quantity: str     # time_of_flight , max_height , range
    value: float

class DifficultyConfig(BaseModel):
    angle: list[int]
    speed: list[int]
