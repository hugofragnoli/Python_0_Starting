import sys

#check filter

mots = ["le", "chat", "est", "grand"]
# La règle : est-ce que la longueur est > 3 ?
resultat = filter(lambda w: len(w) > 3, mots)
print(list(resultat)) 
# Sortie : ['chat', 'grand']

data = [0, 1, False, True, [], [1, 2], "", "Salut"]
# La machine garde tout ce qui a de la "valeur"
resultat = filter(None, data)

print(list(resultat)) 
# Sortie : [1, True, [1, 2], 'Salut']

phrase = "C3P0 est un Dr01de"
# On ne garde que les chiffres
chiffres = filter(str.isdigit, phrase)

print("".join(chiffres)) 
# Sortie : "3001"

points = [[1, 2], [10, 5], [-3, 8], [4, 4]]
# La règle : on garde si x > 0
positifs = filter(lambda p: p[0] > 0, points)

print(list(positifs)) 
# Sortie : [[1, 2], [10, 5], [4, 4]]

nombres = [1, 2, 3]
mon_filtre = filter(lambda x: x > 1, nombres)

print(list(mon_filtre)) # Affiche [2, 3]
print(list(mon_filtre)) # Affiche [] -> IL EST VIDE !