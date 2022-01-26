from package2.hello1 import Hello
from package2.hello4 import HelloAgain

class HelloThere:
    def __init__(self,name):
        self.name = name
    
    def hello1(self):
        print("Hello World {0} from same directory hello3".format(self.name))

def main():
    h1 = Hello("Somal")
    h2 = HelloAgain("Chakraborty")

    h1.hello1()
    h2.hello1()

if __name__ == '__main__':
    main() 