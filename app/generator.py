from app.schemas import ProjectileParams , Problem , DifficultyConfig
from app.solver.projectile import projectile_motion
import random

Difficulty_levels = {
    1: DifficultyConfig(angle=[30,45,60],
                        speed=[20,30,40,50]
                        ),
    2: DifficultyConfig(angle=list(range(20,71)),
                        speed=list(range(10,51))
                        )
}

def generate_problem(difficulty: int = 1) ->Problem:
    config=Difficulty_levels.get(difficulty)
    if config is None:
        raise ValueError(f"Unknown difficulty : {difficulty}")
    angle=random.choice(config.angle)
    speed=random.choice(config.speed)
    params=ProjectileParams(speed=speed,angle=angle)
    solution=projectile_motion(params)
    question=f"A ball is launched at {speed} m/s at {angle} degree above the horizontal. Find the range"

    return Problem(
        id=random.randint(1000,9999),
        topic="Projectile",
        params=params,
        question=question,
        solution=solution
    )


if __name__=="__main__":
    print(generate_problem(1))
    print(generate_problem(2))





