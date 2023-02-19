class Presenter():

    def __init__(self,m, v, type):
        self.view = v
        self.model = m
        self.typeOper = type

    def buttonClick(self):
        a = self.view.getValue("Число 1: ");
        b = self.view.getValue("Число 2: ");
        self.model.setX(a);
        self.model.setY(b);
        result = self.model.result();
        self.view.print(result, self.typeOper );
