from app.solver.projectile import projectile_motion , ProjectileParams 



params=ProjectileParams(speed=10,angle=0.523599)

solution=projectile_motion(params)

print(solution)