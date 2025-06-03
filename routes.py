from app import app
from flask import render_template, request

@app.route('/')
def home():
    return render_template('quizzes.html')

@app.route('/quizzes')
def list_quizzes():
    from models import Quiz
    quizzes = Quiz.query.all()
    return render_template('quizzes.html', quizzes=quizzes)

@app.route('/quiz/<int:id>', methods=['GET', 'POST'])
def take_quiz(id):
    from models import Question
    questions = Question.query.filter_by(quiz_id=id).all()
    if request.method == 'POST':
        score = 0
        for q in questions:
            ans = request.form.get(f"answer_{q.id}", "").strip()
            if ans.lower() == q.correct_answer.lower():
                score += 1
        return render_template('result.html', score=score, total=len(questions))

    return render_template('quiz.html', questions=questions)