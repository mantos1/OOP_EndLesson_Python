from Lesson_7.Model import Model

class CalcModel(Model):
    def __init__(self):
        self.x = 0
        self.y = 0

    def result(self):
        pass

    def setX(self, value):
        self.x = value

    def setY(self, value):
        self.y = value