from app.generator import generate_problem

import pytest

def test_level_1_generator():
    for _ in range(100):
        problem = generate_problem(1)
        assert problem.params.angle in [30,45,60]

def test_level_2_generator():
    for _ in range(500):
        problem = generate_problem(2)
        assert 20 <= problem.params.angle <= 70

def test_level_1_speed():
    for _ in range(100):
        problem = generate_problem(1)
        assert problem.params.speed in [20,30,40,50]

def test_level_2_speed():
    for _ in range (500):
        problem = generate_problem(2)
        assert 10 <= problem.params.speed <= 51

def test_invalid_difficulty():
    with pytest.raises(ValueError):
        generate_problem(5)

