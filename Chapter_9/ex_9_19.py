'''Provided is a list of data about a store’s inventory where each item in the list represents the name of 
an item, how much is in stock, and how much it costs. Print out each item in the list with the same 
formatting, using the .format method (not string concatenation). For example, the first print statment 
should read The store has 12 shoes, each for 29.99 USD.'''

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    litem = item.split()
    product = litem[0]
    stock = litem[1]
    stockwc = stock[:len(stock)-1] #Stock without comma
    price = litem[2]
    product_resume = 'The store has {} {} each for {} USD.'.format(stockwc, product, price)
    print(product_resume)