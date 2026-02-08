import sys
from ft_filter import ft_filter


def main():

    nb_args = len(sys.argv) - 1
    try:
        if nb_args != 2:
            raise AssertionError("the arguments are bad")
        deuxieme_arg = int(sys.argv[2])

    except ValueError:
        raise AssertionError("the arguments are bad")
