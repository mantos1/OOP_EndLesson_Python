from Lesson_7.Presenter import Presenter
from Lesson_7.SumModel import SumModel
from Lesson_7.MultModel import MultModel
from Lesson_7.DiffModel import DiffModel
from Lesson_7.DivideModel import DivideModel
from Lesson_7.View import View

def main_():
    p = Presenter(SumModel(), View(), "sum")
    p.buttonClick()
    p = Presenter(MultModel(), View(), "mult")
    p.buttonClick()
    p = Presenter(DiffModel(), View(), "diff")
    p.buttonClick()
    p = Presenter(DivideModel(), View(), "divide")
    p.buttonClick()
if __name__ == '__main__':
    main_()