import crypt
import secrets
import string

def hash_md5_crypt(password: str, salt: str = None) -> str:
    """
    Hashes a password using MD5 Crypt algorithm with a salt.
    If no salt is provided, a random 8-character salt is generated.
    """
    if salt is None:
        # Génération d'un salt aléatoire de 8 caractères (lettres + chiffres)
        alphabet = string.ascii_letters + string.digits
        salt = ''.join(secrets.choice(alphabet) for _ in range(8))
    
    # Le format '$1$' indique à la fonction crypt d'utiliser MD5
    return crypt.crypt(password, f"$1${salt}")