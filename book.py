
###Public attribut :


### Order Class
class Order:

    global id
    id = 1
    ##Constructor :
    def __init__(self, quantity, price, side, id = 1): 
        self.__quantity = quantity
        self.__price = price
        self.__id = id 
        id = id + 1
        #self.id_order = self.id_order + 1 #at each creation of an order the id is incremented by 1


    ##Methods :

    #Overladed Methods
    def __str__(self): # human-readable content
        return "%s @ %s" % (self.__quantity, self.__price)

    def __repr__(self): # unambiguous representation of the object
        return "Order(id = %s, %s, %s)" % (self.__id, self.__quantity, self.__price)

    def __eq__(self, other): # self == other
        return other and self.__quantity == other.__quantity and self.__price == other.__price

    def __lt__(self, other): # self < other
        return other and self.__price < other.__price





### Book Class:
class Book:
    
    ##Constructor :
    def __init__(self, name): 
        self.__name = name              #Book name
        self.__list_sell_order = []     #list of sell order
        self.__list_buy_order = []      #list of buy order
        self.__id = 1                   #Id of each order
        
    ##Methods :


    #Overladed Methods
    def __str__(self): # human-readable content
        return  "Order Book %s : %s" % (self.__name, [repr(self.__list_sell_order[i]) for i in reversed(range(len(self.__list_sell_order)))])

    #Insert sell order :
    def insert_sell(self, quantity, price):
        ##Creation of the order :
        order = Order(quantity, price, side = "sell")

        ##Insertion of the order (condition):
        for i in range(len(self.__list_sell_order)):

            if order < self.__list_buy_order[i] : 
                self.__list_sell_order.insert(i, order)
                
                break
    
    #Insert buy order :
    def insert_buy(self, quantity, price):
        ##Creation of the order :
        order = Order(quantity, price, side = "buy")

        ##Insertion of the order (condition):
        for i in range(len(self.__list_sell_order)):

            if order > self.__list_buy_order[i] : 
                self.__list_buy_order.insert(i, order)
                
                break

    def show(self):
        for i in range(len(self.__list_sell_order)):
            repr(self.__list_sell_order[i])
        

