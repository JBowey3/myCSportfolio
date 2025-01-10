#james bowey
#conditional statements

#init
#functions
def vote_check():
    age = int(input("please enter your age: "))  #user age prompt
    status = input("are you a US citizen: ")   #user status check
    if age >= 18 and status == "yes":
        print("you can vote!")
    else:
        print("you cannot vote!")
#prints the largest of the 3 numbers abc
def max_num(a, b, c):  #user chooses the numbers
    if a > b and a > c:
        print("A is the largest number with a value of: " + str(a))   #determinant
    if b > a > c:
        print("B is the largest number with a value of: " + str(b))
    if c > a > b:
        print("C is the largest number with a value of: " + str(c))
#  function with a score parameter (use elif if only 1 true in range, stop eval)
def grade_score(score):  #user input
    if score >= 90:
        print("A")     #grade conditions
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score <= 59:  #or just else:
        print("F")
#main
grade_score(43)  #example run for grade conditional

#boolean:
#true or false
#boolean expression: 15 > 10 A statement that evaluates to true or false
# not Inverts the result of a boolean expression
