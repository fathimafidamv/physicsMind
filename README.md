# PhysicsMind

A physics problem generator where **Python computes the answers and an LLM (coming soon) handles the language**.

LLMs often get physics or arithmetic wrong, and a wrong answer key is worse than none. PhysicsMind keeps the ground truth in tested Python code, so every solution is verified. Generative AI is only used for wording, hints and explanations.

## Status

Phase 1 (Python backend) is complete. Phase 2 (LLM layer) is next.

- [x] Pydantic schemas with input validation
- [x] Projectile motion solver (time of flight, max height, range) using Pint for units
- [x] Unit tests, including physical-law checks
- [x] Random problem generator with difficulty levels
- [x] Generator tests (randomised, 100+ runs per level)
- [x] Answer checker with relative tolerance
- [x] FastAPI endpoints (`GET /problem`, `POST /check/{problem_id}`)
- [ ] LLM layer (Groq): word problems, hints, mistake diagnosis
- [ ] Streamlit UI and deployment
- [ ] Persistent storage (PostgreSQL) for problems and student attempts
- [ ] More topics: free fall, Ohm's law, optics

## Tech stack

Python, FastAPI, Pydantic, Pint, SymPy, Pytest. Planned: Groq, Streamlit, PostgreSQL.

## Project structure

```
physicsMind/
├── app/
│   ├── main.py             # FastAPI app
│   ├── schemas.py          # Pydantic models
│   ├── generator.py        # Random problem generator
│   ├── checker.py          # Answer checking with tolerance
│   ├── router/
│   │   └── problem.py      # API endpoints
│   └── solver/
│       └── projectile.py   # Physics solver
├── test/
│   ├── test_projectile.py
│   ├── test_generator.py
│   └── test_checker.py
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/fathimafidamv/physicsMind.git
cd physicsMind
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Run the API

From the project root:

```bash
python -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive API docs.

### Endpoints

**`GET /problem?difficulty=1`** returns a random problem. The solution is hidden from the response.

- Difficulty 1: friendly angles (30°, 45°, 60°)
- Difficulty 2: any integer angle from 20° to 70°
- Any other difficulty returns `400`

Example response:

```json
{
  "id": 4821,
  "topic": "projectile",
  "params": {"speed": 20, "angle": 30, "g": 9.8},
  "question": "A ball is launched at 20 m/s at 30 degrees above the horizontal. Find the range."
}
```

**`POST /check/{problem_id}`** checks a student's answer.

Request body:

```json
{"quantity": "range", "value": 35.4}
```

`quantity` is one of `time_of_flight`, `max_height`, `range`. Response: `{"correct": true}`. Answers within 2% of the true value are accepted, so rounded answers still count. An unknown problem id returns `404` and an unknown quantity returns `400`.

Note: generated problems are currently held in memory, so they are lost when the server restarts.

## Run the tests

From the project root:

```bash
python -m pytest -v
```

## How solutions are verified

- Known values: v = 20 m/s at 30° gives T ≈ 2.04 s, H ≈ 5.10 m, R ≈ 35.35 m.
- Physical laws: 45° gives the maximum range, and complementary angles (30° and 60°) give the same range.
- Input validation: invalid angles and negative speeds are rejected by the schema.
- Generator: parameters are checked against each difficulty's allowed ranges over many random runs.

## Roadmap

The next phase adds an LLM layer using Groq. The LLM turns verified numbers into natural word problems, gives graduated hints, and diagnoses likely mistakes. It never computes answers: every number comes from the tested Python solver.

## Author

Fathima Fida M. V, Physics graduate and Python developer.
[GitHub](https://github.com/fathimafidamv) · [LinkedIn](https://linkedin.com/in/fathima-fidamv)