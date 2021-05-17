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

menu = {
  "Wings":0,
  "Cookies":0,
  "Spring Rolls":0,
  "Salmon":0,
  "Steak":0,
  "Meat Tornado":0,
  "A Literal Garden":0,
  "Ice Cream":0,
  "Cake":0,
  "Pie":0,
  "Coffee":0,
  "Tea":0,
  "Unicorn Tears":0
}

list = []

while True:
    response = input("> ")
    if response == 'quit':
      print("thanks for ordering")
      break
    menu[response] +=1
    order_count = menu[response]
    print(f"""
    {order_count} order of {response} has been added to your meal
    """)

#lab
