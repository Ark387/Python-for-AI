# def count_up_to(n):
#     i=1
#     while i <=n:
#         yield i
#         i= i + 1
    
# gen = count_up_to(100)
# for i in gen:
#     print(i)
    

def shout(func):
    def wrapper(*args):
        print(*args)
        l = list(*args)
        print(l)
        print(l[0],l[1].upper())
        

    return wrapper


@shout
def greet(name):
    print(name)


greet("Hello abdul")