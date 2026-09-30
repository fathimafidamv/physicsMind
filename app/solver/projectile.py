from app.schemas import ProjectileParams , ProjectileSolution
import pint
import math

ureg=pint.UnitRegistry()

def projectile_motion(value:ProjectileParams)->ProjectileSolution:
    v = value.speed *ureg('m/s')
    theta = math.radians(value.angle)
    g = value.g *ureg('m/s**2')

    #Time of flight
    T = (2*v*math.sin(theta))/g
    #Maximum height 
    H = ((v*math.sin(theta))**2)/(2*g)
    #Range
    R =(v**2*math.sin(2*theta))/g

    return ProjectileSolution(
        time_of_flight=T.to('s').magnitude,
        max_height=H.to('m').magnitude,
        range=R.to('m').magnitude
        )