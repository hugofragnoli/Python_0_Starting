import hashlib


def hash_md5_crypt(password: str, salt: str = "default") -> str:
    """
    Hashes a password with MD5 and a salt.
    Works on Python 3.14 without the 'crypt' module.
    """
    # On crée une chaîne combinée : sel + mot de passe
    data = salt + password
    # On génère le hash MD5
    return hashlib.md5(data.encode()).hexdigest()
