import sys

def text_analyzer(text=None):

    if text is None or text == "":
        text = input("What is the text to count?\n")

    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if not c.isalnum() and not c.isspace())
    spc = sum(1 for c in text if c.isspace())
    dig = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spc} spaces")
    print(f"{dig} digits")

def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        
        arg = sys.argv[1] if len(sys.argv) == 2 else None
        text_analyzer(arg)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except EOFError:
        pass

if __name__ == "__main__":
    main()