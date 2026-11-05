def union(A,B):
    return A.union(B)
def intersection(A,B):
    return A.intersection(B)
def difference(A,B):
    return A.difference(B)
def s_d(A,B):
    return A.symmetric_difference(B)

print("***welcome to set operations***")

print("Press 1 for union\nPress 2 for intersection\nPress 3 for difference\nPress 4 for Symmetric difference\n5 for exiting ")

a={1,2,3,4}
b={2,3,6,7}

try:
    while True :
     choice=int(input("enter choice..."))
     match(choice):
         case 1:
             print(union(a,b))
         case 2:
             print(intersection(a,b))
         case 3: 
             print(difference(a,b))
         case 4 :
             print(s_d(a,b))
         case 5 :
             print(" **EXECUTED**")
             break
         case _:
             print("invalid choice")
except ValueError:
    print("invalid value kindly enter number only !")