def my_function_args(*kids):
    """Function to return the youngest child"""
    print("The youngest child is " + kids[2])


def my_function_kwargs(**kid):
    for key, value in kid.items():
        print("%s == %s" % (key, value))

    print("His last name is " + kid["lname"])


def my_function_default_arg(x, y=50):
    print("x: ", x)
    print("y: ", y)




my_function_args("Emil", "Tobias", "Linus")
my_function_kwargs(fname="Tobias", lname="Refsnes")
my_function_default_arg(10)
print(my_function_args.__doc__)

anonymous_function = lambda x: x * x * x
print(anonymous_function(2))
