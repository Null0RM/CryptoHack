from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

# Define the curve
p = 310717010502520989590157367261876774703
a = 2
b = 3

# Generator
g_x = 179210853392303317793440285562762725654
g_y = 105268671499942631758568591033409611165

# Bob's
b_x = 272640099140026426377756188075937988094
b_y = 51062462309521034358726608268084433317

# Alice's
a_x = 280810182131414898730378982766101210916
a_y= 291506490768054478159835604632710368904

from sage.all import *

E = EllipticCurve(GF(p), [a, b])
G = E(g_x, g_y)
B = E(b_x, b_y)
A = E(a_x, a_y)

b = G.discrete_log(B)

shared_secret = (A * b).xy()[0]

data = {'iv': '07e2628b590095a5e332d397b8a59aa7', 'encrypted_flag': '8220b7c47b36777a737f5ef9caa2814cf20c1c1ef496ec21a9b4833da24a008d0870d3ac3a6ad80065c138a2ed6136af'}
iv = data['iv'] # iv
encrypted_flag = data['encrypted_flag'] # encrypt by shared_secret

print(decrypt_flag(shared_secret, iv, encrypted_flag))
