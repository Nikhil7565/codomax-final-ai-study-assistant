# 🧠 StudyAI — Intelligent AI Study Assistant

> An AI-powered learning platform that helps students learn concepts, generate quizzes, create personalized study plans, and prepare for technical interviews.

---

## 🚀 Overview

StudyAI is a complete AI/ML project developed as the final project of the **Codomax Digital Internship**.

The application uses **Google Gemini** to generate personalized educational content based on the student's:

- Subject
- Topic
- Difficulty level
- Selected study mode

Instead of providing the same learning material to every student, StudyAI dynamically generates content according to the learner's requirements.

---

## ✨ Features

### 📚 1. Learn Mode

Generate structured learning material containing:

- Concept explanations
- Key concepts
- Real-world examples
- Technical examples
- Common mistakes
- Quick revision notes
- Practice questions

### 📝 2. Quiz Mode

Generate AI-powered quizzes with:

- Multiple-choice questions
- Four answer options
- Correct answers
- Detailed explanations
- Configurable difficulty

### 🗺️ 3. Study Plan Mode

Generate personalized study roadmaps containing:

- Learning objectives
- Prerequisites
- Topics in learning order
- Practice tasks
- Project ideas
- Revision strategies
- Final checklist

### 💼 4. Interview Prep Mode

Prepare for technical interviews with:

- Core concepts
- Technical interview questions
- Conceptual questions
- Coding/problem-solving questions
- Solutions
- Interview tips
- Quick revision material

---

## 🎨 User Interface

StudyAI provides a modern dashboard-style interface with:

- Dark theme
- Responsive layout
- Sidebar navigation
- Study mode selection
- Subject selection
- Difficulty selection
- AI status indicator
- Learning statistics
- Recent learning sessions
- Downloadable study material

---

## 🧠 AI Workflow

```text
                    ┌──────────────────┐
                    │      Student     │
                    └────────┬─────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Select Subject      │
                  │ Select Difficulty   │
                  │ Select Study Mode   │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Enter Learning Topic│
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Prompt Generation   │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   Google Gemini     │
                  │    AI Model         │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Personalized        │
                  │ Learning Material   │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Student Studies /   │
                  │ Practices / Revises │
                  └─────────────────────┘

```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web application and UI |
| Google Gemini | AI content generation |
| Google GenAI SDK | Gemini API integration |
| Git | Version control |
| GitHub | Source code hosting |

---

## 📁 Project Structure

```text
codomax-final-ai-study-assistant/
│
├── .streamlit/
│   └── config.toml
│
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

> `secrets.toml` is created locally for storing the Gemini API key and is excluded from Git using `.gitignore`.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Nikhil7565/codomax-final-ai-study-assistant.git
```

### 2. Open the project

```bash
cd codomax-final-ai-study-assistant
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Gemini API Key

Create the following file:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

> **Important:** Never upload your API key to GitHub.

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open locally in your browser.

---

## 🔐 Security

The Gemini API key is securely stored using Streamlit Secrets.

The following file is excluded from Git:

```text
.streamlit/secrets.toml
```

The project also uses the following entries in `.gitignore`:

```text
.env
__pycache__/
*.pyc
```

This prevents sensitive configuration files and Python cache files from being committed to the repository.

---

## 📊 Study Modes

```text
StudyAI
│
├── 📚 Learn
│   ├── Explanation
│   ├── Examples
│   ├── Revision
│   └── Practice Questions
│
├── 📝 Quiz
│   ├── MCQs
│   ├── Answers
│   └── Explanations
│
├── 🗺️ Study Plan
│   ├── Objectives
│   ├── Prerequisites
│   ├── Learning Order
│   └── Revision
│
└── 💼 Interview Prep
    ├── Technical Questions
    ├── Conceptual Questions
    ├── Coding Problems
    └── Interview Tips
```

---

## 🎯 Project Objective

The objective of StudyAI is to demonstrate how modern generative AI can be integrated into an educational application to provide personalized learning assistance.

The project combines:

- Python programming
- API integration
- Prompt engineering
- Generative AI
- Web application development
- User interface design
- Session-based application state
- Secure API-key management

---

## 🔮 Future Improvements

Possible future improvements include:

- User authentication
- Persistent user profiles
- Database integration
- Learning progress analytics
- Quiz scoring system
- Personalized recommendations
- PDF/document learning
- Voice-based learning
- AI-generated flashcards
- Deployment on Streamlit Cloud
- Learning streaks and achievements

---

## 🏆 Internship

**Codomax Digital Internship**

### Final AI/ML Project

**Project:** StudyAI — Intelligent AI Study Assistant

---

## 👩‍💻 Author

**Nikhil Agrawal**

B.Tech — Computer Science & Engineering  
GLA University

---

## 📜 License

This project is created for educational and internship purposes.
