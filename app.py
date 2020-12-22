from flask import Flask, escape, request, render_template
from questions import question_selection

app = Flask(__name__)
_selection = question_selection('questions.xml')

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        username = request.form.get('student_name')
        t = _selection.take_question()
    questions = _selection.get_chosen_questions()
    return render_template('questions_list.html', questions = questions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')