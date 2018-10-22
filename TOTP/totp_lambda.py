totp = lambda secret: [
    [
        [
                str(((hmac_hash[offset] & 0x7f) << 24 |
                    (hmac_hash[offset + 1] & 0xff) << 16 |
                    (hmac_hash[offset + 2] & 0xff) << 8 |
                    (hmac_hash[offset + 3] & 0xff)) % 10 ** 6).rjust(6, '0')
            for offset in [hmac_hash[-1] & 0xf]
        ][0]
        for hmac_hash in [sha1_hmac(base32decode(secret.replace(" ", "").upper()), int(time / 30).to_bytes(8, 'big'))]
    ][0]
    for base32decode, sha1_hmac, time in [(
        lambda data: [bytes([int(bits[i * 8:(i + 1) * 8], 2) for i in range(len(bits) // 8)]) for bits in [("".join([bin("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567".index(c))[2:].rjust(5, '0') for c in data.strip("=")]))]][0],
        lambda key, msg: [[sha1(key.translate(bytes(0x5c ^ i for i in range(256))) + sha1(key.translate(bytes(0x36 ^ i for i in range(256))) + msg)) for key in [(key if len(key) <= 64 else sha1(key)).ljust(64, b'\x00')]][0] for sha1 in [lambda data: [([[([w.append(rotate(w[-3] ^ w[-8] ^ w[-14] ^ w[-16], 1)) for _ in range(64)] and False) or [([[[g.__setitem__(j, values[j]) for j in range(5)] for values in [[(rotate(g[0], 5) + [g[3] ^ (g[1] & (g[2] ^ g[3])),g[1] ^ g[2] ^ g[3],(g[1] & g[2]) | (g[1] & g[3]) | (g[2] & g[3]),g[1] ^ g[2] ^ g[3]][i // 20] + g[4] + [0x5A827999,0x6ED9EBA1,0x8F1BBCDC,0xCA62C1D6][i // 20] + w[i]) & 0xffffffff,g[0],rotate(g[1], 30),g[2],g[3]]]] for i in range(80)] and False) or [h.__setitem__(i, (h[i] + g[i]) & 0xffffffff) for i in range(5)] for g in [[_ for _ in h]]] for w in [[int.from_bytes(msg[i_ * 64:(i_ + 1) * 64][i * 4:(i + 1) * 4], 'big') for i in range(16)]]] for i_ in range(len(msg) // 64)] and False) or b''.join([x.to_bytes(4, 'big') for x in h]) for msg, rotate, h in [(data + b'\x80' + b'\x00' * ((56 - (len(data) + 1) % 64) % 64) + (len(data) * 8).to_bytes(8, 'big'),lambda n, b: ((n << b) | (n >> (32 - b))) & 0xffffffff,[0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476,0xC3D2E1F0])]][0]]][0],
        __import__("time").time()
    )]
][0]
