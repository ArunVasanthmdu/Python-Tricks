 
# Function to convert number to text
def convertValue(digit):
    if digit == '0':
        print("Zero ", end = " ")
    elif digit == '1':
        print("One ", end = " ")
    elif digit == '2':
        print("Two ", end = " ")
    elif digit=='3':
        print("Three",end=" ")
    elif digit == '4':
        print("Four ", end = " ")
    elif digit == '5':
        print("Five ", end = " ")
    elif digit == '6':
        print("Six ", end = " ")
    elif digit == '7':
        print("Seven", end = " ")
    elif digit == '8':
        print("Eight", end = " ")
    elif digit == '9':
        print("Nine ", end = " ")
 
# Function to loop through each character in the given number
def changeWord(N):
    i = 0
    length = len(N)
    while i < length:
        convertValue(N[i])
        i += 1
    print("")

movenext="Y"
while movenext=="Y":
  n=input('Please enter a number to convert: ')
  changeWord(n)
  
  movenext = input("Do you want to continue using the converter (Y/N): ")
