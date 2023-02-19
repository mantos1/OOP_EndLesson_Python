class View():

    captionDict = {
        "sum": "Сумма",
        "mult": "Произведение",
        "diff": "Разница",
        "divide": "Отношение"
    }

    def getValue(self, title):
        return int(input(title))

    def print(self, result, typeOper ):
        caption = "";
        for dct in self.captionDict:
            if dct == typeOper:
                print(f"{self.captionDict[dct]}: {result}")