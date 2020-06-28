
print("Welcome to the Maths Calculator!")
print()
marklst = []
def div_set():

    studentID = int(input("Enter the StudentID "))
    tutorialMark = float(input("Enter Assessible Tutorial Mark(/10)"))
    assignmentMark = float(input("Enter Assignment Mark(/100)"))
    examMark = float(input("Enter exam Mark(/150)"))
    finalMark =round(tutorialMark/10*10+assignmentMark/100*20+examMark/150*70)
    print("Student ID :"+ str(studentID)+" Final Marks :"+str(finalMark)+"%")
    lst = [studentID,finalMark]
    marklst.append(lst)
    print()
    anotherStu = input("Would you like to process another student's marks?(y/n)")
    print()
    return anotherStu
ch = 'y'
while ch == 'y':
   ch = div_set()
print("You have processed the following students:")
print("Student ID\t\t\t\t\tFinal Mark (%)")
for x in marklst:
    print("{}\t\t\t\t\t{}".format(x[0],x[1]))
