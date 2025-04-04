def encode_message(secret, cover_text):
    zero_width_chars = {"1": "​", "0": "‌"}  # Invisible characters
    binary_secret = ''.join(format(ord(c), '08b') for c in secret)  # Convert to binary
    hidden_message = "".join(zero_width_chars[b] for b in binary_secret)
    return cover_text + hidden_message  # Append hidden message to normal text

def decode_message(hidden_text):
    zero_width_chars = {"​": "1", "‌": "0"}  # Reverse mapping
    binary_hidden = "".join(zero_width_chars[c] for c in hidden_text if c in zero_width_chars)
    secret_message = "".join(chr(int(binary_hidden[i:i+8], 2)) for i in range(0, len(binary_hidden), 8))
    return secret_message

# Example Usage
cover = input("📩 Enter a normal sentence (cover text): ")
secret = input("🔐 Enter your secret message: ")

encoded_text = encode_message(secret, cover)
print("\n📝 Send this message:", encoded_text)

decoded = decode_message(encoded_text)
print("\n🔍 Decoded Secret Message:", decoded)
