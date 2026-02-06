import sys

#check filter

mots = ["le", "chat", "est", "grand"]
# La règle : est-ce que la longueur est > 3 ?
resultat = filter(lambda w: len(w) > 3, mots)

print(list(resultat)) 
# Sortie : ['chat', 'grand']