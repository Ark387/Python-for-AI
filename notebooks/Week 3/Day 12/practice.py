

def num(user):
        while True:
            try:
                if 0>=user<=120:
                    pass
            
            except ValueError:
                print()
                 
                 
try:
    user = int(input("Enter a number: "))
    num(user)
except ValueError:
    print("Enter a valid Number")
 