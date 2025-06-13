import streamlit as st
from interview_agent import run_interview, evaluate_response

st.set_page_config(page_title="InterviewME", layout="centered")
st.title("🎤 InterviewME - GenAI Mock Interview")

# --- Input fields ---
name = st.text_input("👤 Enter your name:")
Target_company = st.selectbox("🏢 Select Company", ["Amazon", "Uber", "Bharti Airtel", "Facebook", "Infosys", "IBM", "Atlassian"])
round_type = st.selectbox("🎯 Select Round", ["DSA", "HR", "System Design"])

if "history" not in st.session_state:
    st.session_state["history"] = []
if "question" not in st.session_state:
    st.session_state["question"] = ""

# --- Start Interview ---
if st.button("🟢 Start Interview"):
    if name.strip() == "":
        st.warning("Please enter your name before starting.")
    else:
        result = run_interview(name, Target_company, round_type)
        st.session_state["question"] = result["question"]

# --- Display Question and Take Answer ---
if st.session_state["question"]:
    st.subheader("🗣️ Interviewer Question:")
    st.markdown(f"**{st.session_state['question']}**")

    user_answer = st.text_area("✍️ Your Answer:")

    if st.button("✅ Submit Answer"):
        if user_answer.strip() == "":
            st.warning("Please write an answer before submitting.")
        else:
            result = evaluate_response(
                name,
                Target_company,
                round_type,
                st.session_state["question"],
                user_answer
            )
            st.session_state["history"].append(result)
            st.session_state["question"] = ""  # Clear question to avoid repeat

# --- Show Chat History ---
if st.session_state["history"]:
    st.subheader("📜 Interview History")
    for idx, entry in enumerate(st.session_state["history"], 1):
        st.markdown(f"### 🔹 Q{idx}: {entry['question']}")
        st.markdown(f"**You:** {entry['user_answer']}")
        st.markdown(f"**💡 Feedback:** {entry['feedback']}")
        st.markdown("---")
