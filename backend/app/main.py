# Filename: backend/app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from llm_engine import generate_questions, evaluate_answer
from plagiarism_engine import check_plagiarism

app = FastAPI(title="TeachMate Backend API")

class SyllabusRequest(BaseModel):
    syllabus_text: str

class QuestionPaperRequest(BaseModel):
    topics: List[str]
    num_questions: int = 5

class EvaluationRequest(BaseModel):
    question: str
    model_answer: str
    student_answer: str

class PlagiarismRequest(BaseModel):
    answer: str
    corpus: List[str]

@app.post("/generate-questions")
def api_generate(req: QuestionPaperRequest):
    return generate_questions(req.topics, req.num_questions)

@app.post("/evaluate-answer")
def api_evaluate(req: EvaluationRequest):
    return evaluate_answer(req.question, req.model_answer, req.student_answer)

@app.post("/check-plagiarism")
def api_plagiarism(req: PlagiarismRequest):
    return check_plagiarism(req.answer, req.corpus)

@app.get("/")
def root():
    return {"message": "TeachMate Backend Running"}
