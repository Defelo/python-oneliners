def hmac(key: bytes, msg: bytes, hasher: callable) -> bytes:
    if len(key) > 64:
        key = hasher(key)
    key += bytes(64 - len(key))
    opad = bytes(0x5c ^ i for i in range(256))
    ipad = bytes(0x36 ^ i for i in range(256))
    return hasher(key.translate(opad) + hasher(key.translate(ipad) + msg))
