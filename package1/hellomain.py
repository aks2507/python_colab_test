from package2.hello1 import Hello
from package2.hello4 import HelloAgain
from hello3 import HelloThere

def main():
    h1 = Hello("Abhishek")
    h2 = HelloAgain("Kumar")
    h3 = HelloThere("Shukla")

    h1.hello1()
    h2.hello1()
    h3.hello1()

if __name__ == '__main__':
    main()