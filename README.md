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



