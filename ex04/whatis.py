import sys

nb_args = len(sys.argv) - 1

if nb_args > 1:
    print("AssertionError: more than one argument is provided")
    sys.exit()
elif nb_args < 1:
    print("")
    sys.exit()

arg = sys.argv[1]

try:
    nb = int(arg)
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit()

if nb % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
