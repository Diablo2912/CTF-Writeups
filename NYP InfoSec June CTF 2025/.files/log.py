import base64

# Encrypted flag
b64_str = "DxUZPgBsHhdtDRN4C3lsGQNtAn8WF31qfHULcggWJAw8DyAfJgQgDzM="
encrypted = base64.b64decode(b64_str)

# XOR key
key = b"ALIEN_KEY"

# XOR decryption
decrypted = bytes([b ^ key[i % len(key)] for i, b in enumerate(encrypted)])

print(decrypted.decode('utf-8'))
