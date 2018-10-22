def left_rotate(n: int, b: int) -> int:
    return ((n << b) | (n >> (32 - b))) & 0xffffffff


def sha1(data: bytes) -> bytes:
    h = [
        0x67452301,
        0xEFCDAB89,
        0x98BADCFE,
        0x10325476,
        0xC3D2E1F0
    ]
    message = data + b'\x80'
    message += b'\x00' * ((56 - len(message) % 64) % 64)
    message += (len(data) * 8).to_bytes(8, 'big')
    for i_ in range(len(message) // 64):
        chunk = message[i_ * 64:(i_ + 1) * 64]
        w = [int.from_bytes(chunk[i * 4:(i + 1) * 4], 'big') for i in range(16)]
        for i in range(64):
            w.append(left_rotate(w[-3] ^ w[-8] ^ w[-14] ^ w[-16], 1))
        a, b, c, d, e = h
        for i in range(80):
            if i < 20:
                f = d ^ (b & (c ^ d))
                k = 0x5A827999
            elif i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            a, b, c, d, e = (left_rotate(a, 5) + f + e + k + w[i]) & 0xffffffff, a, left_rotate(b, 30), c, d
        h = [(x + y) & 0xffffffff for x, y in zip(h, [a, b, c, d, e])]
    return b''.join([x.to_bytes(4, 'big') for x in h])
