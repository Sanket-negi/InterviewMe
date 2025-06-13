from langgraph.graph import StateGraph, END
from dotenv import load_dotenv
from typing import TypedDict
import google.generativeai as genai
import os

from prompts import generate_question_prompt, generate_evaluation_prompt

# 1. Define the structure of the state
class interviewState(TypedDict):
    name: str
    Target_company: str
    round_type: str
    user_answer: str
    question: str
    feedback: str

# 2. Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 3. Initialize Gemini model
llm = genai.GenerativeModel("gemini-2.0-flash")

# 4. Ask question node
def ask_question(state: interviewState) -> interviewState:
    prompt = generate_question_prompt(state["name"], state["Target_company"], state["round_type"])
    question = llm.generate_content(prompt).text
    state["question"] = question
    return state

# 5. Evaluate answer node
def evaluate_answer(state: interviewState) -> interviewState:
    prompt = generate_evaluation_prompt(state["name"], state["question"], state["user_answer"])
    feedback = llm.generate_content(prompt).text
    state["feedback"] = feedback
    return state

# 6. Run interview - only generates question
def run_interview(name: str, Target_company: str, round_type: str):
    builder = StateGraph(interviewState)
    builder.add_node("ask_question", ask_question)
    builder.set_entry_point("ask_question")
    builder.add_edge("ask_question", END)
    graph = builder.compile()

    init_state = {
        "name": name,
        "Target_company": Target_company,
        "round_type": round_type,
        "user_answer": "",
        "question": "",
        "feedback": ""
    }

    result = graph.invoke(init_state)
    return {
        "question": result["question"]
    }

# 7. Evaluate response - takes answer and returns feedback
def evaluate_response(name: str, Target_company: str, round_type: str, question: str, user_answer: str):
    builder = StateGraph(interviewState)
    builder.add_node("evaluate_answer", evaluate_answer)
    builder.set_entry_point("evaluate_answer")
    builder.add_edge("evaluate_answer", END)
    graph = builder.compile()

    eval_state = {
        "name": name,
        "Target_company": Target_company,
        "round_type": round_type,
        "user_answer": user_answer,
        "question": question,
        "feedback": ""
    }

    result = graph.invoke(eval_state)
    return {
        "question": result["question"],
        "user_answer": result["user_answer"],
        "feedback": result["feedback"]
    }
