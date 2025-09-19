# # Xargs: to handle multiple datas in a single parameter.

def info(*details):
    print(details)
info(23, "arif")


# # sum of 3 with xargs.

def add(*num):
    sum = 0

    for x in num:
        sum = sum + x
    print(sum)
    
add(1,2,3)

# # Xxargs: to handle key and value at the same time.

def data(**details):
    print(details)

data(id=1, name="sakib")