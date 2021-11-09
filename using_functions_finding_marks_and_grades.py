#using_functions_finding_marks_and_grades
def average():
    total=sum(marks)
    subjects=len(marks)
    average=total/subjects
    return average
def grade():
    if average>=90:
        print("a")
    elif average>=80:
        print("b")
    elif average>=70:
        print("c")
marks=[65,54,75,80,65]    
average()
print ("average is ", average)