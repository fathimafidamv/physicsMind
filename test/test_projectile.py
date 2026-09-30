from app.solver.projectile import projectile_motion 
from app.schemas import ProjectileParams

from pydantic import ValidationError
import pytest



def test_projec():

    params=ProjectileParams(speed=20,angle=30)

    solution=projectile_motion(params)

    assert solution.time_of_flight == pytest.approx(2.04 , abs=0.01)
    assert solution.max_height == pytest.approx(5.10 , abs=0.01)
    assert solution.range == pytest.approx(35.35 , abs=0.01)


def test_45_is_max_range():
    r45 = projectile_motion(ProjectileParams(speed=20 , angle=45)).range
    r30 = projectile_motion(ProjectileParams(speed=20,angle=30)).range
    r60 = projectile_motion(ProjectileParams(speed=20,angle=60)).range
    assert r45 > r30
    assert r45 > r60


def test_complementary_angles_same_range():
    r30 = projectile_motion(ProjectileParams(speed=20 , angle=30)).range
    r60 = projectile_motion(ProjectileParams(speed=20 , angle=60)).range
    assert r30 == pytest.approx(r60)

def test_invalid_angle_rejected():
    with pytest.raises(ValidationError):
        projectile_motion(ProjectileParams(speed=20 , angle=90))


def test_negative_speed_rejected():
    with pytest.raises(ValidationError):
        ProjectileParams(speed=-5 , angle=30)

