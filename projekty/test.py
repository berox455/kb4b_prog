#this is a test

import hashlib

inpp = input()
inpp_heshed = hashlib.sha256(bytes(inpp, encoding="utf-8")).hexdigest()

print(inpp_heshed)
