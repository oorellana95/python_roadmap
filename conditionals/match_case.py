"""
python 3.10 or higher
"""

if __name__ == "__main__":
    # Note: As a side note, match and case are better described as “soft” keywords, meaning they only work as keywords
    # in a match case statement.  You can keep using “match” or “case” as a variable name in other parts of your program.
    command = "Goodbye, World!"
    match command:
        case 'Hello, World!':
            print('Hello to you too!')
        case 'Goodbye, World!':
            print('See you later!')
        case _:
            print('No match found')