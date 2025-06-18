# 🎤 InterviewMeAI – GenAI-based Mock Interview Simulator

InterviewMeAI is a LangGraph + LangChain-powered mock interview platform that simulates technical and HR interviews in a conversational format using LLMs.

> 🚀 Built as part of my internship (April–June 2025) under a GenAI-focused team.

---

## 🔍 Features

- 🧠 Context-aware Interview Questions
  Generates questions dynamically based on selected **company** and **interview round** (DSA, HR, System Design).

- ✍️ Answer & Feedback System
  Accepts user input and gives automated scoring + feedback using LLM evaluation prompts.

- 📜 Full Interview History  
  Each question, response, and feedback is logged for review and learning.

- 🎛️ Streamlit UI
  Clean interface for input and interactive chat-style interview experience.

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| `LangGraph` | Manages stateful interview flow using event-driven graph nodes |
| `LangChain` | Handles LLM-based prompting and chaining |
| `OpenAI GPT` | Used for generating and evaluating interview Q&A |
| `Streamlit` | Frontend UI for user interaction |
| `Python` | Core logic and backend functionality |

---

## 🧪 How It Works

1. User enters name, selects target company & round type.
2. LangGraph generates a relevant interview question.
3. User submits an answer.
4. LangChain evaluates the response and gives feedback + score.
5. History of Q&A + evaluation is displayed in the UI.

---

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/05fb77dc-beb0-41fc-986b-c8f24ece6118)

![image](https://github.com/user-attachments/assets/a2a027a8-ab80-4821-bae5-394e7802293a)

![image](https://github.com/user-attachments/assets/3bb34ee0-743f-4868-b522-5d3558bd4848)


---

## 📁 Folder Structure
 InterviewMeAI/
├── app.py # Streamlit app UI
├── interview_agent.py # LangGraph logic
├── prompts.py # Prompt templates
└── README.md

---

## 💡 Future Improvements

- Add voice-to-text support for verbal interviews  
- Include follow-up question chaining based on answer  
- Save/export reports for users

---

## 📬 Connect with Me

Feel free to connect for collaboration or feedback!  
📧 negisanket13@gmail.com

