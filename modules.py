# # Date & Time + math Module

# import datetime
# import math
# import random
# current_datetime = datetime.datetime.now()
# print("Current Date and Time:", current_datetime) 
# #formating
# a= format(current_datetime,"%d-%m-%y")
# print("Formatted Date:", a)

# #square root of 16
# print( math.sqrt(16)) 
 
# #random number between 1 and 50
# a= (random.randint(1,50))
# print("Random Number:", a)
# #power of a number
# b= (math.pow(a,2))
# print("power ", b)

# #square root of 16
# print( "Square root ", math.sqrt(a)) 
# # factorial
# c=math.factorial(a)
# print("factorial ", c)

# #ceil() & floor()
# d=math.ceil(a)
# e=math.floor(a)
# print("Ceil:", d)
# print("Floor:", e)


# #Iterators
# numbers = [1, 2, 3, 4, 5]
# x=iter(numbers)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


# #Generators 
# def numbers():
#     i = 1
#     for i in range(5):
#         yield i
#         i +=1

# y =numbers()   
# print(next(y))
# print(next(y))  
# print(next(y))
# print(next(y)) 
# print(next(y))




# #Closures 
# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function
# message =outer_function("hello")
# message()


# #Decorators
def myfunc(funcs):
    def wrapper ():
        print("before function")
        funcs()
        print("after function")
    return wrapper

@myfunc
def say():
    print("hello world")
myfunc
def says():
    print("hello paras")
say()      
says()
# def count_up(n):
#     i = 1
#     while i <= n:
#         yield i      # pause here!
#         i += 1
# gen = count_up(4)
# print(gen)
# print(gen) # 1
# print(next(gen))   # 2
# print(next(gen))   # 3
# print(next(gen))   # 4
