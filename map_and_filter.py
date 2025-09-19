# # MAP: map received two parameters, first: function, second: list/object.
# and map returns an iterable object so you need to put it in a list
def add(x):
    return x + x

num = [1,2]

res = list(map(add, num))

print(res)


# # Filter: it will return a specific number or data.
# you can use def/lambda
num = [5, 12, 17, 18, 24, 32]

def myFunc(x):
    if x % 2 == 0:
        return True
    else: 
        return False
    
res = list(filter(myFunc, num))
print(res)

# # ---------------------or-----------------
# use can use lamba to make it easier

ages = [5, 12, 17, 18, 24, 32]

res = list(filter(lambda x : x < 12, ages))
print(res)