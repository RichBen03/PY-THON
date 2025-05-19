# BEGIN
#  INTIALIZES A VARIABLE TOTAL TO 0
#  FOR EACH ELEMENT IN THE list
#     SUM TOTAL TO ELEMENT
#  END FOR 
#  return TOTAL
# END

def add(lists):
    total=0
    for element in lists:
        total+=element
    return total
print(add([1,2,3,4]))