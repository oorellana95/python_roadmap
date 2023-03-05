"""
What is Switch statement?

A switch statement is a multiway branch statement that compares the value of a variable to the values specified in case
statements.

Python language doesn’t have a switch statement.

Python uses dictionary mapping to implement Switch Case in Python
"""
def switch_case(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    # Recall from the tutorial on Python dictionaries that the dict.get() method searches a dictionary for the specified
    # key and returns the associated value if it is found, or the given default value if it isn’t.
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    argument = 1
    print (switch_case(argument))