# ft_md5crypt

## Description
A simple Python package that provides MD5 Crypt hashing functionality with salt support. Created for the Piscine Python for Data Science at 42.

## Installation
You can install the package using the following command:
```bash
pip install ./dist/ft_md5crypt-0.0.1-py3-none-any.whl

Usage

from ft_md5crypt.core import hash_md5_crypt

# Standard Unix MD5 Crypt hashing
print(hash_md5_crypt("my_password", "mysalt"))