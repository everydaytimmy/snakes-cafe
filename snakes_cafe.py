print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
***************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
list = []

while True:
    order = input("> ")
    if order == 'quit':
      print("thanks for ordering")
      break
    list.append(order)
    cart = {i:list.count(i) for i in list}
    #print(cart)
    print(f"""
    {cart} order of {order} has been added to your meal
    Type 'quit' to complete your order
    """)
    

#
#
# MyList = ["a", "b", "a", "c", "c", "a", "c"]
# my_dict = {i:MyList.count(i) for i in MyList}
#print my_dict     #or print(my_dict) in python-3.x
# {'a': 3, 'c': 3, 'b': 1}