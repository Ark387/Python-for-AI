
def top_item(n,*sale):
    
    c = 1
    s = sorted(sale,key = lambda p : p[1] , reverse=True)
    l=[]
    for i in s:
        if c <= n:
            l.append(i[0])
            c+=1

    print(l)


top_item(2,("pen",300),("Book",500),("bag",100))
top_item(5,("pen",300),("Book",500),("bag",100))
top_item(2)


class Product:

    def __init__(self,name,price,stock = 0):
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self,Qty):
        self.stock += Qty  

    def sell(self, Qty):
        if self.stock < Qty:
            return False
        self.stock -= Qty
        return True

    def Value(self):
        return self.price * self.stock


pen = Product("Pen",50,10)
print(pen.sell(4), pen.stock)
print(pen.sell(15), pen.stock)
pen.restock(4)
print(pen.Value())

