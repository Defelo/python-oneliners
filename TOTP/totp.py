import base64
import hashlib
import hmac
import random
import time


class TOTP:
    def __init__(self, secret: str):
        self.secret = secret

    def now(self) -> str:
        return self.at(int(time.time() / 30))

    def at(self, for_time: int) -> str:
        secret = base64.b32decode(self.secret)
        hmac_hash = hmac.HMAC(secret, for_time.to_bytes(8, 'big'), hashlib.sha1).digest()
        offset = hmac_hash[-1] & 0xf
        code = ((hmac_hash[offset] & 0x7f) << 24 |
                (hmac_hash[offset + 1] & 0xff) << 16 |
                (hmac_hash[offset + 2] & 0xff) << 8 |
                (hmac_hash[offset + 3] & 0xff))
        out = str(code % 10 ** 6)
        return "0" * (6 - len(out)) + out

    def verify(self, code: str, valid_window: int = 0) -> bool:
        for_time = int(time.time() / 30)
        for i in range(-valid_window, valid_window + 1):
            if self.at(for_time + i) == code.replace(" ", ""):
                return True
        return False

    def generate_uri(self, user: str, issuer: str) -> str:
        return "otpauth://totp/%s?secret=%s&issuer=%s" % (user, self.secret.lower(), issuer)

    @staticmethod
    def generate_random():
        return TOTP("".join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567") for _ in range(16)]))
