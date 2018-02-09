"""
PASS TO HASH!

This basic function is using for hashing passwords which will stored on database.

<salt> is for short passwords. It basicly make password longer. It must be stored somewhere!
<repeat> is the number of hashing. Normaly it is taken as 1000.

"""

from hashlib import sha256

class PassToHash:
    def passToHash(password, salt, repeat):
        # Hash salt and password together.
        _hash = sha256((salt + password).encode('utf-8'))
        for x in range(repeat):
            # Hash salt and password, the salt is previous hash.
            k = _hash.hexdigest() + password
            _hash = sha256(k.encode('utf-8'))
        # return the hash code // 64 character
        return _hash.hexdigest()
