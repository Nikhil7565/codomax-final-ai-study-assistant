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



🛠️ Tech Stack
Technology	Purpose
Python	Application logic
Streamlit	Web application and UI
Google Gemini	AI content generation
Google GenAI SDK	Gemini API integration
Git	Version control
GitHub	Source code hosting
📁 Project Structure
codomax-final-ai-study-assistant/
│
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
│
├── .gitignore
├── app.py
├── requirements.txt
└── README.md

secrets.toml contains the local Gemini API key and is excluded from Git using .gitignore.

⚙️ Installation
1. Clone the repository
git clone https://github.com/Nikhil7565/codomax-final-ai-study-assistant.git
2. Open the project
cd codomax-final-ai-study-assistant
3. Install dependencies
python -m pip install -r requirements.txt
4. Configure Gemini API Key

Create:

.streamlit/secrets.toml

Add:

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

Never upload your API key to GitHub.

5. Run the application
python -m streamlit run app.py

The application will open locally in your browser.

🔐 Security

The Gemini API key is stored using Streamlit secrets.

The following file is excluded from Git:

.streamlit/secrets.toml

The project also uses:

.env
__pycache__/
*.pyc

in .gitignore.

📊 Study Modes
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
🎯 Project Objective

The objective of StudyAI is to demonstrate how modern generative AI can be integrated into an educational application to provide personalized learning assistance.

The project combines:

Python programming
API integration
Prompt engineering
Generative AI
Web application development
User interface design
Session-based application state
Secure API-key management
🔮 Future Improvements

Possible future improvements include:

User authentication
Persistent user profiles
Database integration
Learning progress analytics
Quiz scoring system
Personalized recommendations
PDF/document learning
Voice-based learning
AI-generated flashcards
Deployment on Streamlit Cloud
Learning streaks and achievements
🏆 Internship

Codomax Digital Internship

Final AI/ML Project

Project: StudyAI — Intelligent AI Study Assistant

👩‍💻 Author

Nikhil Agrawal

B.Tech — Computer Science & Engineering
GLA University

📜 License

This project is created for educational and internship purposes.


Then press:

**Ctrl + S**

### Important

Do **not** upload or commit:

```text
.streamlit/secrets.toml

Your .gitignore is already protecting it.

Reply DONE after saving the README.

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
🛠️ Tech Stack
TechnologyPurpose	
Python	Application logic
Streamlit	Web application and UI
Google Gemini	AI content generation
Google GenAI SDK	Gemini API integration
Git	Version control
GitHub	Source code hosting
📁 Project Structure
codomax-final-ai-study-assistant/
│
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
│
├── .gitignore
├── app.py
├── requirements.txt
└── README.md

secrets.toml contains the local Gemini API key and is excluded from Git using .gitignore.

⚙️ Installation
1. Clone the repository
git clone https://github.com/Nikhil7565/codomax-final-ai-study-assistant.git
2. Open the project
cd codomax-final-ai-study-assistant
3. Install dependencies
python -m pip install -r requirements.txt
4. Configure Gemini API Key

Create:

.streamlit/secrets.toml

Add:

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

Never upload your API key to GitHub.

5. Run the application
python -m streamlit run app.py

The application will open locally in your browser.

🔐 Security

The Gemini API key is stored using Streamlit secrets.

The following file is excluded from Git:

.streamlit/secrets.toml

The project also uses:

.env
__pycache__/
*.pyc

in .gitignore.

📊 Study Modes
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
🎯 Project Objective

The objective of StudyAI is to demonstrate how modern generative AI can be integrated into an educational application to provide personalized learning assistance.

The project combines:

Python programming
API integration
Prompt engineering
Generative AI
Web application development
User interface design
Session-based application state
Secure API-key management
🔮 Future Improvements

Possible future improvements include:

User authentication
Persistent user profiles
Database integration
Learning progress analytics
Quiz scoring system
Personalized recommendations
PDF/document learning
Voice-based learning
AI-generated flashcards
Deployment on Streamlit Cloud
Learning streaks and achievements
🏆 Internship

Codomax Digital Internship

Final AI/ML Project

Project: StudyAI — Intelligent AI Study Assistant

👩‍💻 Author

Nikhil Agrawal

B.Tech — Computer Science & Engineering

GLA University

📜 License

This project is created for educational and internship purposes.


Then press:

**Ctrl + S**

### Important

Do **not** upload or commit:

```text
.streamlit/secrets.toml


we paste all this in readme.md

The first commit succeeded. ✅

The second git commit simply says there was nothing new to commit, except README.md still has an unstaged modification.

Step 17 — Stage the latest README

Run:

git add README.md

Then:

git commit -m "Finalize project documentation"

After that, don't push yet. Send me the output.

PS C:\Codomax internship> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& "c:\Codomax internship\.venv\Scripts\Activate.ps1")
(.venv) PS C:\Codomax internship> cd "C:\Codomax internship\codomax-final-ai-study-assistant"                                          
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git remote -v
origin  
Nikhil7565/codomax-final-ai-study-assistant.git (fetch)
origin  
Nikhil7565/codomax-final-ai-study-assistant.git (push)
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        .streamlit/
        app.py
        requirements.txt

no changes added to commit (use "git add" and/or "git commit -a")
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git add README.md .gitignore .streamlit app.py requirements.txt
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git status                                                     
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   .streamlit/config.toml
        modified:   README.md
        new file:   app.py
        new file:   requirements.txt

(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git commit -m "Complete final AI Study Assistant project"
[main 57e10b2] Complete final AI Study Assistant project
 5 files changed, 785 insertions(+), 1 deletion(-)
 create mode 100644 .gitignore
 create mode 100644 .streamlit/config.toml
 create mode 100644 app.py
 create mode 100644 requirements.txt
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git commit -m "Complete final AI Study Assistant project"
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git add README.md
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git commit -m "Finalize project documentation"
[main 89b5bda] Finalize project documentation
 1 file changed, 4 insertions(+), 1 deletion(-)

Perfect 👍 The README changes are now committed successfully.

You now have 2 local commits:

57e10b2 — Complete final AI Study Assistant project
89b5bda — Finalize project documentation
Next step — push everything to GitHub

Run:

git status

Send me the output first. Then we'll push to GitHub.

PS C:\Codomax internship> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& "c:\Codomax internship\.venv\Scripts\Activate.ps1")
(.venv) PS C:\Codomax internship> cd "C:\Codomax internship\codomax-final-ai-study-assistant"                                          
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git remote -v
origin  
Nikhil7565/codomax-final-ai-study-assistant.git (fetch)
origin  
Nikhil7565/codomax-final-ai-study-assistant.git (push)
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        .streamlit/
        app.py
        requirements.txt

no changes added to commit (use "git add" and/or "git commit -a")
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git add README.md .gitignore .streamlit app.py requirements.txt
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git status                                                     
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   .streamlit/config.toml
        modified:   README.md
        new file:   app.py
        new file:   requirements.txt

(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git commit -m "Complete final AI Study Assistant project"
[main 57e10b2] Complete final AI Study Assistant project
 5 files changed, 785 insertions(+), 1 deletion(-)
 create mode 100644 .gitignore
 create mode 100644 .streamlit/config.toml
 create mode 100644 app.py
 create mode 100644 requirements.txt
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git commit -m "Complete final AI Study Assistant project"
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git add README.md
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git commit -m "Finalize project documentation"
[main 89b5bda] Finalize project documentation
 1 file changed, 4 insertions(+), 1 deletion(-)
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git status                                               
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git push  
Enumerating objects: 13, done.
Counting objects: 100% (13/13), done.
Delta compression using up to 12 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (11/11), 5.64 KiB | 2.82 MiB/s, done.
Total 11 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), done.
To 
Nikhil7565/codomax-final-ai-study-assistant.git
   acc114c..89b5bda  main -> main
(.venv) PS C:\Codomax internship\codomax-final-ai-study-assistant> git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

🎉 Perfect! Module 6 GitHub project is successfully pushed.

Your final Git status confirms everything is clean:

Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean

And GitHub received both commits:

57e10b2 — Complete final AI Study Assistant project
89b5bda — Finalize project documentation
✅ Final Project GitHub

codomax-final-ai-study-assistant

🔐 Security check

Your important files are correctly handled:

✅ app.py
✅ README.md
✅ requirements.txt
✅ .gitignore
✅ .streamlit/config.toml
❌ secrets.toml not pushed
❌ Gemini API key not exposed in GitHub
🚀 What remains for Module 6

The technical project is done. Now we should complete the internship submission side:

✅ Final AI/ML project
✅ GitHub repository
✅ README/documentation
⏳ LinkedIn post
⏳ Submit GitHub link + LinkedIn link to Codomax

Next: let's create the final Module 6 LinkedIn post step-by-step.
