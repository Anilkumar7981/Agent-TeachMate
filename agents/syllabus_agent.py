def create_question(topic: str):
    return f"Explain the concept of {topic}."

def generate_question_set(topics, num):
    questions = []
    for i in range(num):
        topic = topics[i % len(topics)]
        q = create_question(topic)
        questions.append(q)
    return questions
