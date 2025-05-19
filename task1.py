# BEGIN
#  INTIALIZES A VARIABLE TOTAL TO 0
#  FOR EACH ELEMENT IN THE list
#     SUM TOTAL TO ELEMENT
#  END FOR 
#  return TOTAL
# END

def add(lists): #Defined a function that takes a list as a parameter
    total=0     #intialized a variable total to 0 to store the sum after each traversal
    for element in lists: # traverse the list and store each number in a variable called element
        total+=element    # sum up the element in the list to the total 
    return total          # return the sum of the list
print(add([1,2,3,4]))     