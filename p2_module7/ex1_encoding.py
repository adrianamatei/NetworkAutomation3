#creat encoder that transforms a > b .....and all spaces to '\n'

"Hello Python. This is converted text."

text = "Hello Python.This is converted text."


result = map(
    lambda c: (
        '\n' if c == ' '
        else chr((ord(c) - ord('A') + 1) % 26 + ord('A')) if c.isupper()
        else chr((ord(c) - ord('a') + 1) % 26 + ord('a')) if c.islower()
        else c
    ),
    text
)
print(type(result))
for ch in result:
    print(ch, end="")
'''  VARIANTAA   ALEXANDRA
# create encoder that transforms a > b .... and all spaces to '\n'

"Hello Pithon. This is converted text."

def encode(s: str) -> str:
    return ''.join(map(lambda ch: '\n' if ch == ' ' else chr(ord(ch) + 1), s))

text = "Hello Pithon. This is converted text"
print(encode(text))
'''