#Draw upper and lower lines
def line1():
    print("+" +  4*'-' + '+' + 4*'-' + '+')

#Draw middle lines
def line2():
    for x in range(4):
        print('|' + 4*' ' + '|' + 4*' ' + '|')

#Repeat drawing lines
def drawsquares():
    line1()
    line2()
    line1()
    line2()
    line1()

#call the function to draw squares
drawsquares()
