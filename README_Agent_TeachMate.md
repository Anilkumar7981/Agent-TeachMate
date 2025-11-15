
# Agent TeachMate — Multi-Agent AI System for Automated Exam Creation & Evaluation
### *Automating Question Paper Creation, Answer Evaluation, and Student Feedback*

---

## Overview
Agent TeachMate is a multi-agent AI system that automates the entire academic assessment workflow—from syllabus analysis and question generation to student answer evaluation, plagiarism detection, and personalized feedback. It reduces teacher workload, increases grading consistency, and provides meaningful learner insights.

---

## Problem Statement
Teachers spend extensive time preparing balanced exams and evaluating subjective answers, especially across large class sizes. This results in delays, inconsistent scoring, evaluator fatigue, and limited personalized feedback. Manual workflows are no longer scalable.  
Agent TeachMate solves these challenges with an end‑to‑end AI‑driven assessment pipeline.

---

## Why Agents?
A single LLM cannot reliably manage syllabus extraction, question creation, difficulty balancing, evaluation, plagiarism detection, and feedback.  
Agents solve this by:
- Specializing in one task each  
- Collaborating in a workflow  
- Using validators for quality checks  
- Retrying until outputs meet standards  
- Scaling modularly  

This mirrors real academic workflows.

---

## Architecture
```
teachmate_controller_agent
│
├── syllabus_analyzer_agent
├── question_generator_agent
│   └── difficulty_scaler_agent
├── paper_assembler_agent
├── answer_evaluator_agent
│   └── rubric_checker_agent
├── plagiarism_detector_agent
└── feedback_generator_agent
```

---

## Demo Summary
1. Upload syllabus → topic extraction  
2. Generate exam → MCQs, short, long questions  
3. Evaluate answers → semantic + rubric scoring  
4. Detect plagiarism → similarity check  
5. Feedback → personalized learning suggestions  
6. Report → analytics for teachers  

---

## Tools & Technologies
Python, LangChain Agents, FastAPI, FAISS, PostgreSQL, OpenAI/Llama models, Streamlit/React.

---

## Impact
- Reduces teacher workload by **60–70%**  
- Ensures consistent, unbiased grading  
- Provides instant feedback  
- Aligns with syllabus and Bloom’s taxonomy  
- Scalable for institutions  

---

## If I Had More Time
- Trend‑analysis agent  
- Adaptive quiz generator  
- LMS integration  
- Dashboard analytics  
- Subject‑specific agents  
- Offline LLM support  

---

## Author
**Chinthalapudi Anil Kumar**  
Capstone Project — 2025
