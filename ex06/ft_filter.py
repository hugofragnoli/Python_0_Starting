# check filter
# lambda -> fonction jetable et anonyme. (elle na pas de nom)
# que l on ecrit sur une seule ligne.
# Cest loutil parfait quand on a besoin dune petite logique
# rapide comme filter().
def ft_filter(function, iterable):
    """
    Réimplémentation de la fonction native filter().

    Cette fonction construit un itérateur à partir des éléments de 'iterable'
    pour lesquels 'function' retourne True.

    Args:
        function (callable | None): Une fonction qui teste chaque élément.
                                    Si None, l'itérateur retourne les éléments
                                    qui sont évalués comme vrais (True).
        iterable (iterable): Un objet itérable (liste, tuple, chaîne, etc.).

    Returns:
        generator: Un itérateur produisant les éléments validés.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
