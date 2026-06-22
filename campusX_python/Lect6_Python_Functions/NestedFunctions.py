# def f():
#   def g():
#     print('inside function g')
#   g()
#   print('inside function f')

# f()

# def f():
#     def g():
#         def e():
#             print("Inside function e ")
#         e()
#         print("Inside function f ")
#     g()
#     print("Inside function g ")

# f()


# become infinte loop 
# def f():
#   def g():
#     print('inside function g')
#     f()
#   g()
#   print('inside function f')

# f()


# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print('in g(x): x =', x)
#     h()
#     return x

# x = 3
# z = g(x)


def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)