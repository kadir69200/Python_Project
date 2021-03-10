
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

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @price.setter
    def price(self, price):
        self.__price = price

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
        already_del = False

        #adding of the order :
        self.__list_sell_order.append(order)

        if len(self.__list_buy_order) != 0 : #the list is not empty

            for i in range(len(self.__list_buy_order)):

                if order.price <= self.__list_buy_order[i].price : 
                    
                    if order.quantity <= self.__list_buy_order[i].quantity : #same price and enough quantity available

                        self.__list_buy_order[i].quantity = self.__list_buy_order[i].quantity - order.quantity #quantity update
            
                        #deletion of the sell order
                        if already_del == False :
                            self.__list_sell_order.remove(order)
                            already_del = True

                        if self.__list_buy_order[i].quantity == 0 : #deletion of the buy order
                            del self.__list_buy_order[i]

                    else : 

                        quantity = order.quantity
                        j = i

                        while True:
                            
                            quantity = quantity - self.__list_buy_order[i].quantity #quantity update
                            
                            self.__list_buy_order[j].quantity = self.__list_buy_order[j].quantity - order.quantity #quantity update
                            del self.__list_buy_order[j]
                            j = j + 1
                            
                            if quantity < self.__list_buy_order[i].quantity :
                                break

                        if already_del == False :
                            self.__list_sell_order.remove(order)
                            already_del = True
                    
                    break
                    
                    


        #Sort of the list (decreasing) :    
        self.__list_sell_order.sort()

    def insert_sell(self, quantity, price):
        ##Creation of the order :
        order = Order(quantity, price, side = "sell")

        ##Insertion of the order (condition):
        self.__list_sell_order.append(order)
        self.__list_sell_order.sort()

        ##Execution :
        #If is not the first order of the book :
        if len(self.__list_sell_order) != 0 and len(self.__list_buy_order) != 0 : #the list are not empty
        
            if self.__list_sell_order[0].price == self.__list_buy_order[0].price and self.__list_sell_order[0].quantity <= self.__list_buy_order[0].quantity : #same price and enough quantity available

                self.__list_buy_order[0].quantity = self.__list_buy_order[0].quantity - self.__list_sell_order[0].quantity #quantity update
            
                #deletion of the sell order
                del self.__list_sell_order[0] 

                if self.__list_buy_order[0].quantity == 0 : #deletion of the buy order
                    del self.__list_buy_order[0]


        

    
    #Insert buy order :
    def insert_buy2(self, quantity, price):
        ##Creation of the order :
        order = Order(quantity, price, side = "buy")
        already_del = False

        ##Insertion of the order (condition):
        self.__list_buy_order.append(order)

        for i in range(len(self.__list_sell_order)):

            if order.price >= self.__list_sell_order[i].price :
            
                if order.quantity <= self.__list_sell_order[i].quantity : #same price and enough quantity available

                    self.__list_sell_order[i].quantity = self.__list_sell_order[i].quantity - order.quantity #quantity update
            
                    #deletion of the buy order
                    if already_del == False :
                        self.__list_buy_order.remove(order)
                        already_del = True

                    if self.__list_sell_order[i].quantity == 0 : #deletion of the sell order
                        del self.__list_sell_order[i]
                

                else : 

                        quantity = order.quantity
                        j = i

                        while True:
                            
                            quantity = quantity - self.__list_sell_order[i].quantity #quantity update
                            
                            self.__list_sell_order[j].quantity = self.__list_sell_order[j].quantity - order.quantity #quantity update
                            del self.__list_sell_order[j]
                            j = j + 1
                            
                            if quantity < self.__list_sell_order[i].quantity :
                                break

                        if already_del == False :
                            self.__list_buy_order.remove(order)
                            already_del = True

                break

        #Sort of the list (decreasing) :    
        self.__list_buy_order.sort(reverse = True)
                

    def insert_buy(self, quantity, price):
        ##Creation of the order :
        order = Order(quantity, price, side = "buy")

        ##Insertion of the order (condition):
        self.__list_buy_order.append(order)
        self.__list_buy_order.sort(reverse = True)

        ##Execution :
        #If is not the first order of the book :
        if len(self.__list_sell_order) != 0 and len(self.__list_buy_order) != 0 : #the list are not empty

            if self.__list_buy_order[0].price == self.__list_sell_order[0].price and self.__list_buy_order[0].quantity <= self.__list_sell_order[0].quantity : #same price and enough quantity available

                self.__list_sell_order[0].quantity = self.__list_sell_order[0].quantity - self.__list_buy_order[0].quantity #quantity update
            
                #deletion of the buy order
                del self.__list_buy_order[0] 

                if self.__list_sell_order[0].quantity == 0 : #deletion of the sell order
                    del self.__list_sell_order[0]




        

