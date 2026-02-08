import sys


def main():
    # type dict vaut map en c++ -. key / value
    MORSE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.'
        }
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        premier_arg = sys.argv[1]
        # on leve une erreur si nimporte quel char nest ni alnum nio isspace
        # avec any des quon en trouve un on arrete alors que si on faisait une
        # somme et un if qui dit si char_spé > 1 on doit parcourir tout larg.
        if any(not c.isalnum() and not c.isspace() for c in premier_arg):
            raise AssertionError("the arguments are bad")

        encrypted_message_list = []
        for char in premier_arg.upper():
            if char.isspace():
                encrypted_message_list.append("/")
            else:
                encrypted_message_list.append(MORSE_DICT[char])

        print(" ".join(encrypted_message_list))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
