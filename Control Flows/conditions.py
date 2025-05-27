marks = int(input("Enter your marks in percentage: "))
output = ""

if(marks<30):
    output= "You have failed the exams"
elif(marks>30 and marks<40):
    output = "You have a grade D"
elif(marks>40 and marks <60):
    output = "You gave a grade C"
elif(marks>60 and marks <70):
    output="You have a grade B"
elif(marks>70):
    output="You have a grade A"

print(output)

# Match-Case Statements

