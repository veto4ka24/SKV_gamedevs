class Question():
    def __init__(self,quest, yes, no):
          self.quest=quest
          self.yes=yes
          self.no=no
    def next(self,answer):
        if answer=='yes':
            return self.yes
        else:
            return self.no


