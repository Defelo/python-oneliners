sha1 = lambda data: [
    ([
         [
             ([
                  w.append(rotate(w[-3] ^ w[-8] ^ w[-14] ^ w[-16], 1))
                  for _ in range(64)
              ] and False) or [
                 ([
                      [
                          [
                              g.__setitem__(j, values[j])
                              for j in range(5)
                          ]
                          for values in [[
                              (rotate(g[0], 5) + [
                                  g[3] ^ (g[1] & (g[2] ^ g[3])),
                                  g[1] ^ g[2] ^ g[3],
                                  (g[1] & g[2]) | (g[1] & g[3]) | (g[2] & g[3]),
                                  g[1] ^ g[2] ^ g[3]
                              ][i // 20] + g[4] + [
                                   0x5A827999,
                                   0x6ED9EBA1,
                                   0x8F1BBCDC,
                                   0xCA62C1D6
                               ][i // 20] + w[i]) & 0xffffffff,
                              g[0],
                              rotate(g[1], 30),
                              g[2],
                              g[3]
                          ]]
                      ]
                      for i in range(80)
                  ] and False) or [
                     h.__setitem__(i, (h[i] + g[i]) & 0xffffffff)
                     for i in range(5)
                 ]
                 for g in [[_ for _ in h]]
             ]
             for w in [[int.from_bytes(msg[i_ * 64:(i_ + 1) * 64][i * 4:(i + 1) * 4], 'big') for i in range(16)]]
         ]
         for i_ in range(len(msg) // 64)
     ] and False) or b''.join([x.to_bytes(4, 'big') for x in h])
    for msg, rotate, h in [(
        data + b'\x80' + b'\x00' * ((56 - (len(data) + 1) % 64) % 64) + (len(data) * 8).to_bytes(8, 'big'),
        lambda n, b: ((n << b) | (n >> (32 - b))) & 0xffffffff,
        [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0
        ]
    )]
][0]
