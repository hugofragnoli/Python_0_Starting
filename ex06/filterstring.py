import sys
from ft_filter import ft_filter


def main():
    """
    Filters words from string S with length strictly greater than N.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        try:
            n_min = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        s_arg = sys.argv[1]

        # Ici on crée une fonction invisible.
        # lambda word = ecrire def function(word)
        # On definit que notre func prend un arg "word"
        # len(word) > n_min -> cest le test :
        # La focntion calcule la len du mot et compare a n_min
        # Une lambda renvoie true ou false en fonction du res.
        # Si len > n_min -> true
        def check_len(word):
            return len(word) > n_min
        result = [w for w in ft_filter(check_len, s_arg.split())]
        # List comprehension contrainte
        # .split() pour isoler les mots
        # s.arg.split(decoupe arg 1 en une liste de mots indiv)
        # for w in : -> boucle-> on prend chaque mot et on le passe a filter
        # chaque mot sappelle w temporairement.
        # ft_filter parcourt chaque mot et demande a lambda si cest true ou pas
        # si true, ft_filter garde le mot dans son iterateur.
        # le result est un type list
        # pour montrer si on me demande
        # type_result = type(result)
        # print(f"type de result est {type_result}")

        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
