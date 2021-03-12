
###Public attribut :

import pandas as pd
import numpy as np

### Order Class
class Order:
    
    id = 1
    ##Constructor :
    def __init__(self, quantity, price, side):
        self.__quantity = quantity          #Volume of the order
        self.__price = price                #Price of the order
        self.__side = side                  #Type of order (BUY or SELL)
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
        return "Order(id = %s, %s, %s)" % (self.__id, self.__quantity, self.__price)

    def __repr__(self): # unambiguous representation of the object
        return "%s  %s @ %s  id = %s" % (self.__side, self.__quantity, self.__price, self.__id)

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
        self.__sells_dataframe = pd.DataFrame(columns=['price','quantity'])
        self.__buys_dataframe = pd.DataFrame(columns=['price','quantity'])
        
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
    
    @property
    def sells_dataframe(self):
        return self.__sells_dataframe
    @property
    def buys_dataframe(self):
        return self.__buys_dataframe
    
    ###Methods :


    ##Overladed Methods
    def __str__(self): # human-readable content
        # sells=np.array([order.price,order.id] for order in self.__list_sell_order )
        # sell_dataframe=pd.DataFrame(sells,[order.id for order in self.__list_sell_order ],['price','volume'])
        # sell_dataframe.sort_values(by = 'price',ascending = False)

        # buys=np.array([order.price,order.id] for order in self.__list_buy_order )
        # buy_dataframe=pd.DataFrame(buys,[order.id for order in self.__list_buy_order ],['price','volume'])
        # buy_dataframe.sort_values(by = 'price',ascending = False)
        
        # for order in self.__list_sell_order:
        #     sell=pd.DataFrame([(order.price,order.quantity)],index=[order.id],columns=['price','quantity'])
        #     self.__sells_dataframe=self.__sells_dataframe.append(sell)
        
        # for order in self.__list_buy_order:
        #     buy=pd.DataFrame([(order.price,order.quantity)],index=[order.id],columns=['price','quantity'])
        #     self.__buys_dataframe=self.__buys_dataframe.append(buy)
        
        
        if (self.__sells_dataframe.empty == False) or(self.__buys_dataframe.empty == False):
            print("TABULA REPRESENTATION")
            print("---------------------")
            print("---ASK---")
            print(self.__sells_dataframe)
            print("---BID---")
            print(self.__buys_dataframe)
        
        return  str("Book on %s : \n        " %(self.__name) + 
                "\n        ".join( repr(order) for order in self.__list_sell_order ) + 
                "\n        "+"\n        ".join( repr(order) for order in self.__list_buy_order ))
        

    
    ##Insert sell order :

    def insert_sell(self, quantity, price):
        
        ##Creation of the order :
        order = Order(quantity, price, side = "SELL")
        
        already_del = False #order already deleted
        execution = False #to know if there has been an execution or not
        executed_order = []

        #adding of the order :
        self.__list_sell_order.append(order)
        

        if len(self.__list_buy_order) != 0 : #the list is not empty

            for i in range(len(self.__list_buy_order)):

                if order.price <= self.__list_buy_order[i].price : 

                    execution = True


                    if order.quantity <= self.__list_buy_order[i].quantity : #same price and enough quantity available

                        self.__list_buy_order[i].quantity = self.__list_buy_order[i].quantity - order.quantity #quantity update
            
                        #deletion of the sell order
                        if already_del == False :
                            self.__list_sell_order.remove(order)
                            already_del = True

                        if self.__list_buy_order[i].quantity == 0 : #deletion of the buy order
                            del self.__list_buy_order[i]

                        executed_order.append((self.__list_buy_order[i].quantity, self.__list_buy_order[i].price))

                    else : 

                        quantity = order.quantity
                        j = i

                        while True:
                            
                            quantity = quantity - self.__list_buy_order[i].quantity #quantity update
                            
                            self.__list_buy_order[j].quantity = self.__list_buy_order[j].quantity - order.quantity #quantity update
                            del self.__list_buy_order[j]
                            
                            executed_order.append((quantity, self.__list_buy_order[j].price))

                            j = j + 1

                            if quantity < self.__list_buy_order[i].quantity :
                                break

                        if already_del == False :
                            self.__list_sell_order.remove(order)
                            already_del = True
                    
                    break
                    
                    
        #Sort of the list :    
        self.__list_sell_order.sort()
        
        ##Display of the order book :
        if execution == False : 
            print("-------------------------------------------\n--- Insert "+ repr(order) +" on %s" % (self.__name) + '\n' + self.__str__() + 
                 "\n-------------------------------------------\n")
            
            
            # sell=pd.DataFrame([(price,quantity)],index=[order.id],columns=['price','quantity'])
            # self.__sells_dataframe=self.__sells_dataframe.append(sell)

        else :
            print("-------------------------------------------\n--- Insert "+ repr(order) +" on %s" % (self.__name) + '\n' + 
                "\n" .join("Execute "+ str(order[0]) + " at " + str(order[1]) + " on " + self.__name for order in executed_order ) +
                '\n' + self.__str__() +  "\n-------------------------------------------\n")  
            
    
    
    
    def insert_sell2(self, quantity, price):
        ##Creation of the order :
        order = Order(quantity, price, side = "SELL")

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
    def insert_buy(self, quantity, price):
        
        ##Creation of the order :
        order = Order(quantity, price, side = "BUY")
        
        already_del = False #order already deleted
        execution = False #to know if there has been an execution or not
        executed_order = []

        ##Insertion of the order (condition):
        self.__list_buy_order.append(order)

        for i in range(len(self.__list_sell_order)):

            if order.price >= self.__list_sell_order[i].price :

                execution = True
            
                if order.quantity <= self.__list_sell_order[i].quantity : #same price and enough quantity available

                    self.__list_sell_order[i].quantity = self.__list_sell_order[i].quantity - order.quantity #quantity update
            
                    #deletion of the buy order
                    if already_del == False :
                        self.__list_buy_order.remove(order)
                        already_del = True

                    if self.__list_sell_order[i].quantity == 0 : #deletion of the sell order
                        del self.__list_sell_order[i]

                    executed_order.append((self.__list_sell_order[i].quantity, self.__list_sell_order[i].price))

                else : 

                        quantity = order.quantity
                        j = i

                        while True:
                            
                            quantity = quantity - self.__list_sell_order[i].quantity #quantity update
                            
                            self.__list_sell_order[j].quantity = self.__list_sell_order[j].quantity - order.quantity #quantity update
                            del self.__list_sell_order[j]
                            
                            executed_order.append((quantity, self.__list_sell_order[j].price))
                            
                            j = j + 1
                            
                            if quantity < self.__list_sell_order[i].quantity :
                                break

                        if already_del == False :
                            self.__list_buy_order.remove(order)
                            already_del = True

                break

        #Sort of the list (decreasing) :    
        self.__list_buy_order.sort(reverse = True)

        ##Display of the order book :
        if execution == False : 
            
            print("-------------------------------------------\n--- Insert "+ repr(order) +" on %s" % (self.__name) + '\n' + self.__str__() + 
                 "\n-------------------------------------------\n")
            
            
            # buy=pd.DataFrame([(price,quantity)],index=[order.id],columns=['price','quantity'])
            # self.__buys_dataframe=self.__buys_dataframe.append(buy,ignore_index=True)
        else :
            print("-------------------------------------------\n--- Insert "+ repr(order) +" on %s" % (self.__name) + '\n' + 
                "\n" .join("Execute "+ str(order[0]) + " at " + str(order[1]) + " on " + self.__name for order in executed_order ) +
                '\n' + self.__str__() +  "\n-------------------------------------------\n")  
                

    
    
    def insert_buy2(self, quantity, price):
        ##Creation of the order :
        order = Order(quantity, price, side = "BUY")

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




        

