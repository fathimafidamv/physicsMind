import streamlit as st
import requests

API_URL = "https://physicsmind.onrender.com"



def fetch_problem(difficulty: int) -> dict:
    try:
        response = requests.get(f"{API_URL}/problem" , 
                            params = {"difficulty": difficulty},
                            timeout=60)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e :
        st.error(f"Error fetching problem: {e}")
        return None

def submit_answer(problem_id: int, quantity: str, value: float) -> dict:
    try:
        response = requests.post(f"{API_URL}/check",
                            json = {
                                "problem_id": problem_id,
                                "quantity": quantity,
                                "value": value,
                            },
                            timeout=60)
        if response.status_code == 422:
            st.error(f"Invalid request: {response.json()['detail']}")
            return None
                     
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error submitting answer: {e}")
        return None

st.title("Physics Assistant")
st.markdown("Welcome to the Physics Assistant! This app helps you solve physics problems and understand concepts.")

difficulty = st.selectbox("Difficulty Level", [1,2])

if st.button("New Problem"):
    with st.spinner("Loading. The first request can take up to a minute."):
        new_problem = fetch_problem(difficulty)
    if new_problem is not None:
        st.session_state["problem"] = new_problem
problem = st.session_state.get("problem")
if problem:
    st.write(problem["question"])
    quantity = st.selectbox("Select Quantity", ["time_of_flight", "max_height", "range"])
    value = st.number_input("Enter your answer:", step=0.01 , format = "%.2f")

    if st.button("Check"):
        result = submit_answer(problem["id"],quantity,value)
        if result is True:
            st.success("Correct answer!")
        elif result is False:
            st.error("Incorrect answer.Check  your formula and try again!")

