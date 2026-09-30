from fastapi import FastAPI
from app.router.problem import router as problem_router


app=FastAPI()
app.include_router(problem_router)

@app.get("/")
def home():
    return{
        "message":"Physics Mind API"
    }
