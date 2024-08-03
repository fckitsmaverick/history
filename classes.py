class Question:
    def __init__(self, question, answer, period, score):
        self.question = question
        self.answer = answer
        self.period = period
        self.score = score

    def addHint(self, hint):
        self.hint = hint

    def showQuestion(self):
        print(self.question)

class Period:
    def __init__(self, period):
        self.period = period