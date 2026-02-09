import os
import time

def ft_tqdm(lst: range) -> None:
    """
    Copie simplifiée de tqdm utilisant yield.
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
        bar_str = ('=' * (filled - 1) + '>').ljust(bar_size) if filled > 0 else '>'.ljust(bar_size)
        
        # CONSTRUCTION DE LA LIGNE UNIQUE
        # Le \r doit être le TOUT PREMIER caractère imprimé ( retour chariot)
        output = f"\r{int(percent)}%|[{bar_str}]| {current}/{total} [{elapsed:.2f}s<{eta:.2f}s, {speed:.2f}it/s]"
        
        print(output, end="", flush=True)
        
        yield item
    
    # Saut de ligne final une fois la boucle terminée
    print()