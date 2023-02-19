from Lesson_7.CalcModel import CalcModel

class DiffModel(CalcModel):

    def setX(self, value):
        CalcModel.x = value

    def setY(self, value):
        CalcModel.y = value

    def result(self):
        return CalcModel.x - CalcModel.y
