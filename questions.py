from random import randint
import xml.etree.ElementTree as ET

class question_selection():
    def __init__(self, filename):
        root = ET.parse(filename).getroot()
        questions = []
        for child in root:
            questions.append(child.text)
        self._base_questions = questions
        self._chosen_questions = []

    def take_question(self):
        num_questions = len(self._base_questions)
        if num_questions==0:
            return None
        rand = randint(0, num_questions-1)
        question = self._base_questions.pop(rand)
        self._chosen_questions.insert(0, question)
        return question
    
    def get_base_questions(self):
        return self._base_questions

    def get_chosen_questions(self):
        return self._chosen_questions 