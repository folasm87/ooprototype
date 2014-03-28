import re
import pdb

class Order(object):
    
    def __init__(self, customer, order_no, shipping_addr, items):
        self.customer = customer
        self.order_no = order_no
        self.shipping_addr = shipping_addr
        self.items = items
    
    def get_customer(self):
        return self.customer
    
    def get_order_no(self):
        return self.order_no
    
    def get_shipping_addr(self):
        return self.shipping_addr
    
    def get_items(self):
        return self.items

class Customer(object):
    
    def __init__(self, name, age, phone_number, credit_card, billing_addr, shipping_addr, orders):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.credit_card = credit_card
        self.billing_addr = billing_addr
        self.shipping_addr = shipping_addr
        self.orders = orders
    
    def same_customer(self, name, age, phone_number, credit_card, billing_addr, shipping_addr):
        if((self.name == name) and (self.age == age) and (self.phone_number == phone_number) and (self.credit_card == credit_card) and (self.billing_addr == billing_addr) and (self.shipping_addr == shipping_addr)):
            return True
        return False
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_credit_card(self):
        return self.credit_card
    
    def get_billing_addr(self):
        return self.billing_addr
    
    def get_shipping_addr(self):
        return self.shipping_addr
    
    def get_orders(self):
        return self.orders

def new_order(customer, order_no, shipping_addr, items):
    return Order(customer, order_no, shipping_addr, items)
    
def new_customer(name, age, phone_number, credit_card, billing_addr, shipping_addr, orders):
    return Customer(name, age, phone_number, credit_card, billing_addr, shipping_addr, orders)

def validate_info(info_type, info):
    
    namePattern = re.compile('\d|\s+')
    
    #Source: http://www.diveintopython.net/regular_expressions/phone_numbers.html
    phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)
    
    #Source: http://www.regular-expressions.info/creditcard.html
    credit_card_Pattern = re.compile(r'''
     ^(?:4[0-9]{12}(?:[0-9]{3})?         # Visa
     |  5[1-5][0-9]{14}                  # MasterCard
     |  3[47][0-9]{13}                   # American Express
     |  3(?:0[0-5]|[68][0-9])[0-9]{11}   # Diners Club
     |  6(?:011|5[0-9]{2})[0-9]{12}      # Discover
     |  (?:2131|1800|35\d{3})\d{11}      # JCB
     )$
    ''', re.VERBOSE)
    
    if(info_type == "name"):
        return bool(namePattern.search(info))#False if it contains a number or a space
    elif(info_type == "phone"):
        return bool(phonePattern.search(info))
        
    elif(info_type == "age"):
        info = int(info)
        if(info in range(18,120)):
            return True
    elif(info_type == "credit card"):
        return bool(credit_card_Pattern.search(info))
    
    return False
def print_order(order):
    for item in order.get_items():
        print "{0}".format(item)
    print "\n"

def print_customer(customer):
    print "\n"
    print "Name: {0}".format(customer.get_name()) 
    print "Age: {0}".format(customer.get_age())
    print "Credit Card: {0}".format(customer.get_credit_card())
    print "Billing Address: {0}".format(customer.get_billing_addr())
    print "Shipping Address: {0}".format(customer.get_shipping_addr())
    print "-"*16 + "Orders" + "-"*21
    i = 0
    for order in customer.get_orders():
        i += 1
        print "Order #{0}:".format(i)
        print "-"*10
        print_order(order)

def customer_input():
    first_name = ' '
    while(validate_info("name", first_name)):
        first_name = raw_input("What is your First name (no spaces please): ")
    
    last_name = ' '
    while(validate_info("name", last_name)):
        last_name = raw_input("What is your Last name (no spaces please): ")
    
    cust_age = '1'
    while(not validate_info("age", cust_age)):
        cust_age = raw_input("What is your age (18 to 120): ")
        
    cust_phone = ' '
    while(not validate_info("phone", cust_phone)):
        cust_phone = raw_input("What is your Phone Number: ")
        
    cust_credit_card = ' '
    while(not validate_info("phone", cust_credit_card)):
        cust_credit_card = raw_input("What is your credit card number please: ")
        
    
    cust_billing_addr = raw_input("What is your Billing Address please: ")
    cust_shipping_addr = raw_input("What is your Shipping Address please: ")

    return {"name": first_name+" "+last_name, "age": cust_age, "phone": cust_phone, "credit": cust_credit_card, "billing": cust_billing_addr, "shipping": cust_shipping_addr}

def main():
    
    customers = {}
 
    new_customer_data = True
    
    while(new_customer_data or (len(customers) == 0)): #we handle new customers OR no customers at all
        cust = {}
        returning_customer = 'no'
        same_customer = False
        if(len(customers) > 0):
            returning_customer = ''
            while(returning_customer != 'yes' and returning_customer != 'no'):
                returning_customer = raw_input("Are you a returning customer? (yes or no) ")
                returning_customer = returning_customer.lower()
                if(returning_customer == 'no'):
                    cust = customer_input()
                    
                elif(returning_customer == 'yes'):
                    
                    first_name = ' '
                    while(validate_info("name", first_name)):
                        first_name = raw_input("What is your First name (no spaces please): ")
                    
                    last_name = ' '
                    while(validate_info("name", last_name)):
                        last_name = raw_input("What is your Last name (no spaces please): ")
                    
                    if(customers.has_key(first_name + " " + last_name)):
                        cust = customers[first_name + " " + last_name]
                        same_customer = True
                    else:
                        print "\n"
                        print "Sorry, we have no previous records with that name"
                        returning_customer = 'no'
                        cust = customer_input()
                    
        else:
            cust = customer_input()

        if(not(same_customer)):
            cust_orders = []
        
        order_again = True
        add_item = True
        order_num = 0
        place_new_order = 'yes'
        while((order_again and place_new_order == 'yes') or order_num == 0):
            order_num = order_num + 1
            items = []
            add_another_item = 'yes'
            while(add_item and add_another_item == 'yes'):
                new_item = raw_input("What item would you like to add to your order? ")
                items.append(new_item)
                
                add_another_item = raw_input("Would you like to add another item to your order? (YES or NO): ")
                add_another_item = add_another_item.lower()
                if(add_another_item == 'yes'):
                    add_item = True
                elif(add_another_item == 'no'):
                    add_item = False
                    print "You chose not to add another item"
            
            if(same_customer):
                customers[cust.get_name()].orders.append((new_order(cust.get_name(), order_num, cust.get_shipping_addr(), items)))
                print "You are a returning customer"
            else:
                cust_orders.append(new_order(cust['name'], order_num, cust['shipping'], items))
            
            place_new_order = raw_input("Would you like to place a new order? ")
            place_new_order = place_new_order.lower()
            if(place_new_order == 'yes'):
                order_again = True
                add_item = True
                add_another_item == 'yes'
                print "You are ordering again"
                
            elif(place_new_order == 'no'):
                order_again = False
                print "No new orders"
        
        if(not(same_customer)):
            customers.setdefault(cust['name'], new_customer(cust['name'], cust['age'], cust['phone'], cust['credit'], cust['billing'], cust['shipping'], cust_orders))
        
        for k,v in customers.items():
            print_customer(v)
        
if __name__ == '__main__':  
   main()