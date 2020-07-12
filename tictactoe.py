def updateboard():
    '''
    this function updates the tictactoe board
    '''
    if(move1==1):
def printboard():
    print("    |   |    ")
    print("  a | b | c  ")
    print("____|___|____")
    print("    |   |    ")
    print("  d | e | f  ")
    print("____|___|____")
    print("    |   |    ")
    print("  g | h | i  ")
    print("    |   |    ")
printboard();
p1=input("->Player One:Whart do you want(O or X):")
p2=''
if(p1=='O'):
    p2='X'
    print("->Player Two:You are given X")
elif(p1=='X'):
    p2='O'
    print("->Player Two:You are given O")
else:
    print("You entered wrong information...")
move1=int(input("->Player One,Enter your move:"))
updateboard()
printboard()
move2=int(input("->Player Two,Enter your move:"))
updateboard()
printboard()
