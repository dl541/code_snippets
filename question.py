class Question:
    def __init__(self,q,a1,a2,a3,a4,ca):
        self.question=q
        self.answer1=a1
        self.answer2=a2
        self.answer3=a3
        self.answer4=a4
        self.correct=ca

    def printQandA(self): # should use 'print' instead of 'get' here. 'get' implies that the function will return something but this function doesn't
        print(self.question)
        print(self.answer1)
        print(self.answer2)
        print(self.answer3)
        print(self.answer4)
