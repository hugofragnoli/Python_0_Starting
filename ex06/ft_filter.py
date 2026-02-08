# check filter
# lambda -> fonction jetable et anonyme. (elle na pas de nom)
# que l on ecrit sur une seule ligne.
# Cest loutil parfait quand on a besoin dune petite logique
# rapide comme filter().
def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
