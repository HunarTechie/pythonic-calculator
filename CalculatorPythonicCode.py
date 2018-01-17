import sys
print("*"*45,'\n',"*"*7,"welcome to my github account","*"*7)
print("*"*45)
print("*"*10,"calculator","*"*10,'\n'"lets start..")
action = input("select an operation! (add-sub-mul-div)")
x = int(input("please give first number"))
y = int(input("please give second number"))
while True:

    def Print():
        if action.lower() == "add":
            print(ADD())
        elif action.lower() == "sub":
            print(SUB())
        elif action.lower() == "mul":
            print(MUL())
        elif action.lower() == "div":
            print(DIV())
        elif action.lower() == "exit":
            print(EXIT())

    def ADD():
        return '{} + {} = '.format(x, y), (x + y)

    def SUB():
        return '{} + {} = '.format(x, y), (x - y)

    def MUL():
        return '{} + {} = '.format(x, y), (x * y)

    def DIV():
        return '{} + {} = '.format(x, y), (x / y)

    Print()

    action = input("select an operation! (add-sub-mul-div-exit)")
    if action.lower() == 'exit':
        def EXIT():
           sys.exit()
    else:
        x = int(input("please give first number"))
        y = int(input("please give second number"))
