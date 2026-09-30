# PhysicsMind

A physics problem generator where **Python computes the answers and an LLM (coming soon) handles the language**.

LLMs often get physics or arithmetic wrong, and a wrong answer key is worse than none. PhysicsMind keeps the ground truth in tested Python code, so every solution is verified. Generative AI is only used for wording, hints and explanations.

## Status

Work in progress.

- [x] Pydantic schemas with input validation
- [x] Projectile motion solver (time of flight, max height, range) using Pint for units
- [x] Unit tests, including physical-law checks
- [ ] Random problem generator with difficulty levels
- [ ] Answer checker with tolerance
- [ ] FastAPI endpoints (`GET /problem`, `POST /check`)
- [ ] LLM layer (Groq): word problems, hints, mistake diagnosis
- [ ] Streamlit UI and deployment
- [ ] More topics: free fall, Ohm's law, optics

## Tech stack

Python, Pydantic, Pint, SymPy, Pytest. Planned: FastAPI, Groq, Streamlit, PostgreSQL.

## Project structure

```
physicsmind/
├── app/
│   ├── schemas.py          # Pydantic models
│   └── solver/
│       └── projectile.py   # Physics solver
├── test/
│   └── test_projectile.py
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/fathimafidamv/physicsmind.git
cd physicsmind
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Run the tests

Run from the project root:

```bash
python -m pytest -v
```

## Example

```python
from app.schemas import ProjectileParams
from app.solver.projectile import projectile_motion

solution = projectile_motion(ProjectileParams(speed=20, angle=30))
print(solution)
# time_of_flight=2.04 max_height=5.10 range=35.35
```

## How solutions are verified

- Known values: v = 20 m/s at 30° gives T ≈ 2.04 s, H ≈ 5.10 m, R ≈ 35.35 m.
- Physical laws: 45° gives the maximum range, and complementary angles (30° and 60°) give the same range.
- Input validation: invalid angles and negative speeds are rejected by the schema.

## Author

Fathima Fida M. V, Physics graduate and Python developer.
[GitHub](https://github.com/fathimafidamv) · [LinkedIn](https://linkedin.com/in/fathima-fidamv)
