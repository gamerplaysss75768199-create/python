def data(data):
 try:
  n=int(input("enter how many students u want to add : "))
 except ValueError:
   print("kindly enter integer value only")
 else :
  count=len(data)+1
  for i in range(n):
    name=input(f"enter name for {i+1} student: ")
    marks=[]
    for j in range(3):
        marks.append(int(input(f"enter marks in subject {j+1}: ")))

    data[count]={name:marks}
    count+=1


def search(data):
 try:
  n=int(input("enter the name roll number of the student u want the data of : "))
 except ValueError:
   print("kindly enter numbers only")
 else:
  print(data[n])

def average(data):
  highest_average=0
  for roll,details in data.items():
    for name,marks in details.items():
     avrg=sum(marks)/3
     if(highest_average<avrg):
       highest_average=avrg
       studentr=roll
       studentn=name
  print(f"The student with the higest avrg is roll number: {studentr}\n name ={studentn}")



students={}
print("**WELCOME TO STUDENT MANAGEMENT SYSTEM**")
while True :
 x=int(input("1 for addding student\n2 for print data\n3 for searching a student\n4 for displaying student with highest average\n0 to exit "))
 match(x):
   case 1 :
    print("\n")
    data(students)
    print("\n")
    print("\n")
   case 0 :
      print("\n")
      print("**THANKS FOR USING**")
      break
   case 2:
     print("\n")
     for i in students.items():
       print (i)
     print("\n")
     print("\n")

   case 3:
     print("\n") 
     search(students)
     print("\n")
     print("\n")
   case 4 :
     print("\n")
     average(students)
     print("\n")
     print("\n")
   case _:
     print("\n")
     print("INVALID CHOICE")