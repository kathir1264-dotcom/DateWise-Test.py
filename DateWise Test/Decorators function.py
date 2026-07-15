# def decorator(func):
#     def wrapper(result):
#         print("welcone")
#         func(result)
#         print("thank you")
#     return wrapper
# @decorator
# def name(result):
#     print("hi",result)
# name("kathir")

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("hello")
#         func(*args, **kwargs)
#         print("bye")
#     return wrapper
# @decorator
# def name(result):
#     print("hi",result)
# name("kathir")

def decorator(func):
    def value(*args,**kwargs):
        print("add")
        func(*args, **kwargs)
        print("integer")
    return value
@decorator
def numbers():
    print(5+10)
numbers()