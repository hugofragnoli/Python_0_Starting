from datetime import datetime


# Pour obtenir la date et l'heure précises maintenant
maintenant = datetime.now()

print(f"Date non formatée : {maintenant}")

format_special = maintenant.strftime("%b %d %Y")
# %d minuscule pour le day comme ca, %b pour le mois et pas %m (02) et %Y
# pour lannee en affichage standard

print(f"{format_special}")  # et on print
