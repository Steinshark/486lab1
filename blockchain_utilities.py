from hashlib import sha256
from json import loads, dumps
from requests import get, post

# CONSTANTS INITIALISED HERE
HASHER = {'SHA256' : sha256()}



# FILE MANIPULATION FUNCTIONS
def import_JSON_dict(json_fname):
    json_text = open(json_fname).read()
    return json.loads(json_text)

# HASHING FUNCTIONS
def hash(alg,format,bytes):
    HASHER[alg].update(bytes)
    digest = HASHER[alg].digest()
    if format == 'hex':
        return digest.hex()
    elif format == 'bytes':
        return digest

#
def
