import os
import streamlit as st
from google import genai

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="StudyAI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 85% 5%, rgba(124, 58, 237, 0.16), transparent 28%),
        radial-gradient(circle at 15% 30%, rgba(59, 130, 246, 0.10), transparent 25%),
        #080b12;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: #0b0f17;
    border-right: 1px solid #1f2937;
}

.block-container {
    max-width: 1380px;
    padding-top: 2rem;
}

/* Sidebar */

.sidebar-brand {
    padding: 10px 4px 24px;
}

.sidebar-logo {
    font-size: 28px;
    font-weight: 800;
}

.sidebar-subtitle {
    color: #64748b;
    font-size: 13px;
    margin-top: 4px;
}

.sidebar-section {
    color: #64748b;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-top: 25px;
    margin-bottom: 10px;
    text-transform: uppercase;
}

/* Main header */

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 28px;
}

.page-title {
    font-size: 34px;
    font-weight: 800;
    color: #f8fafc;
}

.page-subtitle {
    color: #94a3b8;
    margin-top: 5px;
}

.status {
    background: #111827;
    border: 1px solid #263244;
    padding: 9px 15px;
    border-radius: 999px;
    color: #cbd5e1;
    font-size: 13px;
}

/* Cards */

.card {
    background: rgba(15, 23, 42, 0.82);
    border: 1px solid #1f2937;
    border-radius: 20px;
    padding: 22px;
    margin-bottom: 18px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.20);
}

.card:hover {
    border-color: #334155;
}

.card-label {
    color: #94a3b8;
    font-size: 13px;
}

.card-value {
    color: #f8fafc;
    font-size: 27px;
    font-weight: 800;
    margin-top: 7px;
}

.card-icon {
    font-size: 22px;
}

/* Hero */

.hero {
    background:
        linear-gradient(135deg,
        rgba(30, 41, 59, 0.96),
        rgba(17, 24, 39, 0.92));
    border: 1px solid #293548;
    border-radius: 24px;
    padding: 30px;
    margin-bottom: 22px;
}

.hero-title {
    font-size: 30px;
    font-weight: 800;
    color: #f8fafc;
}

.hero-text {
    color: #94a3b8;
    margin-top: 8px;
    line-height: 1.6;
}

/* Input */

.input-card {
    background: #0f172a;
    border: 1px solid #263244;
    border-radius: 20px;
    padding: 24px;
}

.input-title {
    font-size: 19px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 6px;
}

.input-description {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 15px;
}

/* Native text area */

textarea {
    background: #0b1220 !important;
    color: #f8fafc !important;
    border: 1px solid #334155 !important;
    border-radius: 14px !important;
}

textarea:focus {
    border-color: #8b5cf6 !important;
}

/* Buttons */

.stButton > button {
    border-radius: 12px;
    min-height: 44px;
    font-weight: 700;
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    border: none;
    color: white;
}

.stButton > button:hover {
    box-shadow: 0 0 25px rgba(139, 92, 246, 0.28);
}

/* Result */

.result-header {
    font-size: 22px;
    font-weight: 800;
    color: #f8fafc;
    margin: 25px 0 14px;
}

.result-box {
    background: #0f172a;
    border: 1px solid #1f2937;
    border-radius: 20px;
    padding: 28px;
    line-height: 1.75;
}

/* Recent */

.recent-item {
    background: #0f172a;
    border: 1px solid #1f2937;
    border-radius: 16px;
    padding: 17px;
    margin-bottom: 10px;
}

.recent-title {
    color: #e2e8f0;
    font-weight: 700;
}

.recent-meta {
    color: #64748b;
    font-size: 12px;
    margin-top: 4px;
}

/* Footer */

.footer {
    text-align: center;
    color: #475569;
    font-size: 12px;
    padding: 30px 0 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "result" not in st.session_state:
    st.session_state.result = ""

# =========================================================
# API KEY
# =========================================================

api_key = None

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key is not configured.")
    st.stop()

client = genai.Client(api_key=api_key)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-logo">🧠 StudyAI</div>
        <div class="sidebar-subtitle">
            Intelligent learning workspace
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section">Workspace</div>',
                unsafe_allow_html=True)

    mode = st.radio(
        "Study mode",
        [
            "📚 Learn",
            "📝 Quiz",
            "🗺️ Study Plan",
            "💼 Interview Prep"
        ],
        label_visibility="collapsed"
    )

    st.markdown('<div class="sidebar-section">Preferences</div>',
                unsafe_allow_html=True)

    subject = st.selectbox(
        "Subject",
        [
            "Computer Science",
            "Artificial Intelligence",
            "Machine Learning",
            "Data Science",
            "Cloud Computing",
            "Programming",
            "General"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Beginner", "Intermediate", "Advanced"],
        index=1
    )

    st.markdown('<div class="sidebar-section">Session</div>',
                unsafe_allow_html=True)

    st.metric(
        "Topics studied",
        len(st.session_state.history)
    )

    st.markdown("---")

    st.caption("Powered by Google Gemini")
    st.caption("Codomax Digital Internship • Final Project")

# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="topbar">
        <div>
            <div class="page-title">Study Dashboard</div>
            <div class="page-subtitle">
                Learn, practice and prepare with your personal AI tutor.
            </div>
        </div>
        <div class="status">● AI Assistant Online</div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# STATS
# =========================================================

c1, c2, c3, c4 = st.columns(4)

stats = [
    ("🧠", "AI Tutor", "Gemini Powered"),
    ("📚", "Study Modes", "4 Available"),
    ("🎯", "Difficulty", difficulty),
    ("∞", "Topics", "Unlimited")
]

for column, (icon, label, value) in zip(
    [c1, c2, c3, c4],
    stats
):

    with column:

        st.markdown(
            f"""
            <div class="card">
                <div class="card-icon">{icon}</div>
                <div class="card-label">{label}</div>
                <div class="card-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">👋 What are you learning today?</div>
        <div class="hero-text">
            Enter any concept, technical topic, interview question,
            or subject. StudyAI will create personalized learning
            material based on your selected mode and difficulty.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# INPUT
# =========================================================

st.markdown("""
<div class="input-card">

<div class="input-title">
🎯 Learning Topic
</div>

<div class="input-description">
Enter the topic you want StudyAI to work on.
</div>

</div>
""", unsafe_allow_html=True)

topic = st.text_area(
    "Learning topic",
    placeholder=(
        "Example: Explain Neural Networks with a real-world example..."
    ),
    height=130,
    label_visibility="collapsed"
)

generate = st.button(
    "✨ Generate Learning Material",
    use_container_width=True
)

# =========================================================
# PROMPT
# =========================================================

def build_prompt():

    if mode == "📚 Learn":

        return f"""
You are an expert AI tutor.

Subject: {subject}
Topic: {topic}
Difficulty: {difficulty}

Create high-quality study material.

Use these sections:

# Concept Explanation
# Key Concepts
# Real-World Example
# Technical Example
# Common Mistakes
# Quick Revision
# Practice Questions

Make the explanation accurate, structured and useful for a student.
"""

    if mode == "📝 Quiz":

        return f"""
You are an expert technical quiz generator.

Subject: {subject}
Topic: {topic}
Difficulty: {difficulty}

Create exactly 10 MCQs.

For every question include:

Question
A.
B.
C.
D.
Correct Answer
Explanation

Make the questions test understanding.
"""

    if mode == "🗺️ Study Plan":

        return f"""
You are an expert academic mentor.

Subject: {subject}
Topic: {topic}
Difficulty: {difficulty}

Create a practical study roadmap.

Include:

# Learning Objectives
# Prerequisites
# Topics in Learning Order
# Practice Tasks
# Project Ideas
# Revision Strategy
# Final Checklist
"""

    return f"""
You are an expert technical interviewer.

Subject: {subject}
Topic: {topic}
Difficulty: {difficulty}

Prepare the student for technical interviews.

Include:

# Core Concepts
# Technical Interview Questions
# Conceptual Questions
# Common Interview Mistakes
# Interview Tips
# Quick Revision Sheet
"""

# =========================================================
# GENERATE
# =========================================================

if generate:

    if not topic.strip():

        st.warning("Please enter a topic first.")

    else:

        try:

            with st.spinner(
                "🧠 StudyAI is preparing your material..."
            ):

                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=build_prompt()
                )

            st.session_state.result = response.text

            st.session_state.history.append({
                "topic": topic,
                "mode": mode,
                "subject": subject
            })

        except Exception as e:

            message = str(e)

            if "503" in message or "UNAVAILABLE" in message:

                st.warning(
                    "Gemini is temporarily busy. "
                    "Please try again in a moment."
                )

            else:

                st.error(
                    "Unable to generate the response."
                )

# =========================================================
# RESULT
# =========================================================

if st.session_state.result:

    st.markdown(
        '<div class="result-header">📖 AI Learning Result</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        st.markdown(st.session_state.result)

    st.download_button(
        "📥 Download Study Material",
        st.session_state.result,
        file_name="study_material.txt",
        mime="text/plain"
    )

# =========================================================
# RECENT SESSIONS
# =========================================================

if st.session_state.history:

    st.markdown("## 🕘 Recent Learning")

    recent = list(reversed(st.session_state.history[-3:]))

    for item in recent:

        with st.container(border=True):

            st.markdown(
                f"### 📚 {item['topic']}"
            )

            st.caption(
                f"{item['subject']} • {item['mode']}"
            )

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    StudyAI • Built with Python, Streamlit & Google Gemini
    <br>
    Codomax Digital Internship • Final AI/ML Project
</div>
""", unsafe_allow_html=True)