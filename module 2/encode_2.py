def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        code = ord(char)
        shifted_code = (code + shift) % 256
        result =result +  chr(shifted_code)
    return result

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        code = ord(char)
        shifted_code = (code - shift) % 256
        result =result + chr(shifted_code)
    return result

# Test
original = "hello python"
shift = 3

encrypted = caesar_encrypt(original, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Original :", original)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
