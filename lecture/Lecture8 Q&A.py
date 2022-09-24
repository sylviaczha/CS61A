def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

cascade(54321)


#Q: what is the difference between recursion and self-reference?

# recursion
def f(x):
    f(x)

f(3)

#self-reference

#A: Recursion involves making a call to f within the body of f.
# Recursion can kick off a whole chain of computation.
# The function will be called multiple times each time we call it.
# Many of the recursions could have done with while statements.
# We can do multiple recursive calls within the body of a function.


# Self-reference is using the name of the function that have been defined somewhere within the body.
# Self-reference will not kick off a whole chain of computation.
# The function will only be called once each time we call it.


#Q: what about self-reference where the self reference is within a function within a function?

def f(x):
    def g(y):
        f(y)
    return g

# By calling f(x) or g(x), we do not get a whole chain of computation.
# We are going to have only one thing happen.
# If f is called, return g.
# If g is called, return f.



#Q: under what circumstances, do we need mutual recursions?

#A: when every other item (e.g. digit, character) is treated differently.
# We have to keep track of the digit.
# By calling a function every other time, we have a sense of state without explicitly holding onto a variable to do that.


#Q: Iterative solution of luhn algorithms.
#A:
def luhn_sum(n):
    double = False
    the_sum = 0
    while n > 0:
        if double:
            ...
            double = '''switching to another state'''
        else:
            ...
            double = '''switching to another state'''
    return the_sum
