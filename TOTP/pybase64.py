import base64
import os
import string

charset = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"


def base64encode(data: bytes) -> str:
    bits = "".join([bin(c)[2:].rjust(8, '0') for c in data]) + "0" * ((3 - len(data)) % 3 * 2)
    chunks = [bits[i * 6:(i + 1) * 6] for i in range(len(bits) // 6)]
    return "".join([charset[int(c, 2)] for c in chunks]) + "=" * ((3 - len(data)) % 3)


def base64decode(data: str) -> bytes:
    padding = data.count("=")
    data = data.strip("=")
    bits = "".join([bin(charset.index(c))[2:].rjust(6, '0') for c in data])
    if padding:
        bits = bits[:-padding * 2]
    return bytes([int(bits[i * 8:(i + 1) * 8], 2) for i in range(len(bits) // 8)])


def test(inp: bytes, enc: callable, enc2: callable, dec: callable):
    print("Input:", inp)
    my = enc(inp)
    print("My Output:", my)
    correct = enc2(inp).decode()
    print("Correct Output:", correct)
    if my == correct:
        dec = dec(my)
        print("Decoded:", dec)
        print(dec == inp)
    else:
        print(False)


test(os.urandom(385), base64encode, base64.b64encode, base64decode)
