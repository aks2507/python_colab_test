class HelloAgain:
    def __init__(self,name):
        self.name = name
    
    def hello1(self):
        print("Hello there {0}. from nested package2.hello4! Nice to see you once again!!".format(self.name))