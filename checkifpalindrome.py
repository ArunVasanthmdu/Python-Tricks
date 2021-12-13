
#function to check the given string
def checkifpalindrome(mystring):
  # make it suitable for caseless comparison
  mystring = mystring.casefold()
  
  # reverse the string
  revstring = reversed(mystring)
  
  # check if the string is equal to its reverse
  if list(mystring) == list(revstring):
    print("The string is a palindrome.")
  else:
    print("The string is not a palindrome.")


movenext="Y"
while movenext=="Y":
  instring=input('Please enter a text to check if it is palindrome: ')
  checkifpalindrome(instring)
  movenext = input("Do you want to continue using the converter (Y/N): ")
