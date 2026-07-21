# 1) Create a class named `Computer`.
class Computer:
# 2) Define the constructor `__init__(self)`:
#    a) Initialize a private instance variable `self.__maxprice = 900`.
#    (Double underscore makes it private/name-mangled.)
    def __init__(self):
        self.__maxprice = 900
# 3) Define a method `sell(self)`:
#    a) Print the current selling price using `self.__maxprice`.
    def sell(self):
        print ("Selling Price {}: ".format(self.__maxprice))
# 4) Define a setter method `setMaxPrice(self, price)`:
#    a) Update the private variable `self.__maxprice` with the new value `price`.
    def setMaxPrice(self, price):
        self.__maxprice = price
# 5) Create an object `c` of the class `Computer`.
c = Computer()
# 6) Call `c.sell()` to display the initial selling price (900).
c.sell()
# 7) Try to change the price directly using `c.__maxprice = 1000`:
#    a) This does NOT update the private variable `self.__maxprice`.
#    b) Instead, it creates a new attribute named `__maxprice` outside the class’s private one.
c.__maxprice = 1000
# 8) Call `c.sell()` again:
#    a) It still prints 900 because the original private variable was not changed.
c.sell()
# 9) Update the price properly using the setter method:
#    a) Call `c.setMaxPrice(1000)` to modify `self.__maxprice`.
c.setMaxPrice(1000)
# 10) Call `c.sell()` again:
#     a) It now prints 1000 because the private variable was updated using the setter.
c.sell()