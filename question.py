class Replica():
    def __init__(self,rep):
          self.replica=rep

class Question(Replica):
    def __init__(self, rep, yes, no):
          self.replica=rep
          self.yes=yes
          self.no=no
    def next(self,answer):
        if answer=='yes':
            return self.yes
        else:
            return self.no


