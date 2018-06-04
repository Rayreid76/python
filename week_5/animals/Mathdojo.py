class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            self.result += i
        print str(self.result)
        return self


    def subtract(self, *args):
        for i in args:
            self.result -= i
        print str(self.result)
        return self

      


md = MathDojo()

md.add(2).add(2,5).subtract(3,2).result