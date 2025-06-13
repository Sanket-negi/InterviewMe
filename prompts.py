def generate_question_prompt(name,company, round_type):
    return f"""Hi {name}
You are a technical interviewer at {company}.
Ask a single {round_type} interview question appropriate for a candidate with 0-1 years of experience.Act like a proper tech interviewer not like an AI or llm
"""

def generate_evaluation_prompt(name,question, answer):
    return f"""
You asked the following interview question: "{question}"

The candidate answered: "{answer}"

Evaluate the answer. Give a score out of 10 and brief feedback on what was good and what could be improved.
"""