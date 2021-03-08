
###Public attribut :


### Order Class
class Order:
    
    id = 1
    ##Constructor :
    def __init__(self, quantity, price, side):
        self.__quantity = quantity          #Volume of the order
        self.__price = price                #Price of the order
        self.__id = Order.id                #Id of each order
        Order.id = Order.id + 1             #at each creation of an order the id is incremented by 1
        
    ##Property :

    @property
    def quantity(self):
        return self.__quantity
    
    @property
    def price(self):
        return self.__price

    @property
    def Id(self):
        return self.__id

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
              

    ##Property :
        
    @property
    def name(self):
        return self.__name 

    @property
    def list_sell_order(self):
        return self.__list_sell_order

    @property
    def list_buy_order(self):
        return self.__list_sell_order

      
    ##Methods :


    #Overladed Methods
    def __str__(self): # human-readable content
        return  "Order Book %s : \n ------------------------- \n ASK %s \n BID %s" % (self.__name, self.__list_sell_order, self.__list_buy_order)

    #Insert sell order :
    def insert_sell2(self, quantity, price):
        ##Creation of the order :
        order = Order(quantity, price, side = "sell")

        ##Insertion of the order (condition):

        #if it is the first order of the book :
        if len(self.__list_sell_order) == 0 :
            self.__list_sell_order.append(order)
            
        
        else :
            for i in range(len(self.__list_sell_order)):

                if order < self.__list_buy_order[i] : 
                    self.__list_sell_order.insert(i, order)
                
                    break

    def insert_sell(self, quantity, price):
        ##Creation of the order :
        order = Order(quantity, price, side = "sell")

        ##Insertion of the order (condition):
        self.__list_sell_order.append(order)
        self.__list_sell_order.sort()
        

    
    #Insert buy order :
    def insert_buy2(self, quantity, price):
        ##Creation of the order :
        order = Order(quantity, price, side = "buy")

        ##Insertion of the order (condition):
        for i in range(len(self.__list_sell_order)):

            if order > self.__list_buy_order[i] : 
                self.__list_buy_order.insert(i, order)
                
                break

    def insert_buy(self, quantity, price):
        ##Creation of the order :
        order = Order(quantity, price, side = "buy")

        ##Insertion of the order (condition):
        self.__list_buy_order.append(order)
        self.__list_buy_order.sort(reverse = True)


        

