import os
import time


def ft_tqdm(lst: range) -> None:
    """
    Décorateur de boucle simulant la barre de progression de la biblio tqdm.

    Cette fonction est un générateur qui enveloppe une itération, calcule les
    statistiques de performance en temps réel et les affiche dans le terminal
    sur une seule ligne dynamique.

    Args:
        lst (range): Une séquence d'éléments à itérer.

    Yields:
        item: L'élément actuel de la séquence originale.

    Calculs effectués :
        - Pourcentage : Progression relative par rapport au total.
        - Barre de chargement : Visualisation graphique adaptée à la largeur
        du terminal.
        - Elapsed Time : Temps écoulé depuis le début de la première itération.
        - ETA (Estimated Time of Arrival) : Temps restant estimé
        basé sur la vitesse actuelle.
        - Speed (it/s) : Nombre d'itérations traitées par seconde.
    """
    total = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst):
        current = i + 1
        elapsed = time.time() - start_time
        percent = (current / total) * 100
        speed = current / elapsed if elapsed > 0 else 0
        eta = (total - current) / speed if speed > 0 else 0

        # On récupère la largeur pour que ça reste sur une seule ligne
        columns = os.get_terminal_size().columns
        bar_size = max(columns - 45, 5)

        filled = int(bar_size * current // total)
        # Construction de la barre [===>    ]
        if filled > 0:
            bar_str = ('=' * (filled - 1) + '>').ljust(bar_size)
        else:
            bar_str = '>'.ljust(bar_size)

        # CONSTRUCTION DE LA LIGNE UNIQUE
        # Le \r doit être le TOUT PREMIER caractère imprimé ( retour chariot)
        stats = f"{current}/{total} [{elapsed:.2f}s<{eta:.2f}s, "
        stats += f"{speed:.2f}it/s]"
        output = f"\r{int(percent)}%|[{bar_str}]| {stats}"

        print(output, end="", flush=True)

        yield item

    # Saut de ligne final une fois la boucle terminée
    print()
