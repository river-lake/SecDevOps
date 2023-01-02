import base64
from Crypto.Cipher import AES
from Crypto.Util import Padding
from Crypto import Random

# An iv must be an unpredictable number
# iv = Random.get_random_bytes(AES.block_size)
iv = bytes(AES.block_size)

# A symmetric key must be an unpredictable number and it cannot be hardcoded
# key = Random.get_random_bytes(AES.block_size)
key = bytes(AES.block_size)

data = b"secret data"

raw = bytes(Padding.pad(data_to_pad=data, block_size=AES.block_size))
cipher = AES.new(key, AES.MODE_CBC, iv)

print("The encrypted input")
print(base64.b64encode(iv + cipher.encrypt(raw)))
