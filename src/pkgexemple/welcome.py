def int_randomizer():
    """
    This function will always return 42 (int), test: /test/test_welcome.py

    Extended description of function should be placed here, yet there is not
    much to say about this one...

    Returns
    -------
    int
        will always be 42
    """

    return 42

def say_hello():
    """This function print a simple welcome message to the user

    Returns
    -------
    None
        just a message in terminal :
        \"Welcome to this complicated tutorial, World\"
    """

    print "Welcome to this complicated tutorial, World"

def say_something(arg1):
    """This function print a message to the user, which can be choose

    Parameters
    ----------
    arg1 : type optional
        The first parameter. It will automatiquelly be converted to string.

    Returns
    -------
    str
        \"Hello World, I must tell you something: \", arg1
    """

    strReturned = "Hello World, I must tell you something: "  + str(arg1) +"."

    print strReturned
    return strReturned

def _private_function():
    """This one will never appear in the documentation beause of
    the \"_\" before it's name yet I can write it doc.

    Returns
    -------
    None
        just a message in terminal:
        \"This is a secret function, dont use it too much =)\"

    """
    print "This is a secret function, dont use it too much =)"


def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value
    """

    return True

say_hello()
say_something(4)
say_something("I just call to say : \"I love you\" ")
