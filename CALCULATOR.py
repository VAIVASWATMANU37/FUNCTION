print("CHOOSE WHAT YOU WANT TO CALCULATE:")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
SRT = int(input("ENTER YOUR CHOICE"))
A1 = int(input("ENTER THE FIRST NO."))
A2 = int(input("ENTER THE SECOND NO."))
def ADD():
    print(A1 + A2)
def SUB():
    print(A1 - A2)
def MUL():
    print(A1 * A2)
def DIV():
    print(A1 / A2)
if SRT == 1:
    ADD()
elif SRT == 2:
    SUB()
elif SRT == 3:
    MUL()
elif SRT == 4:
    DIV()
else:
    print("ERROR 69420!!!" 
          "INVALID CHOICE!!!")