#default arguments=A default value for certain parameters
#default is used when that argument is omited make your functions more flexible,reduces of arguments

def net_price(list_price,discount=0,tax=0.05):
    return list_price*(1-discount)*(1+tax)

#print(net_price(500,0,0.05))
#print(net_price(500))
#print(net_price(500,0.1,))
print(net_price(500,0.1,0))