import crypt_backend

c = crypt_backend.encrypt("Hello!")
print(f"Encode: {c}")

d = crypt_backend.decrypt(c)
print(f'Decode: {d}')