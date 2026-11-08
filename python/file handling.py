def read(name):
    with open (name , 'r') as f :
        data=f.read()
        print(data)

def write(name):
    with open (name,'w')as f :
        f.write(input("enter..."))

def append(name):
    with open(name ,'a') as f :
        f.write(input("enter..."))

def delete(name):
    with open(name , 'w') as f :
        pass
    print("deleted")

while True :
 x=int(input("1 to read\n2 to write\n3 to append\n4 to delete\n5 for exiting"))
 name=input("enter file name ")
 match(x):
    case 1:
        read(name)
    case 2 :
        write(name)
    case 3:
        append(name)
    case 4 :
        delete(name)
    case 5 :
        print("**executed**")
        break 
    case _:
        print("invalid choice")