#Shahfareeze bin Ramlee
#Program checks the grade for student

def determine_grade (mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"
    

mark = float(input("Enter the student's mark:"))
print (f"Mark: {mark}, Grade: {determine_grade(mark)}")
