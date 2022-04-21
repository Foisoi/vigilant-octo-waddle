def xor(numbers, key):
    chars = []
    for i in range(0, len(numbers)):
        chars.append(numbers[i] ^ key[i % min(len(key), len(numbers))])
    return chars


def stringify(chars):
    result = ""
    for s in chars:
        result += chr(s)
    return result


print("String ords:", " ".join(list(map(lambda x: str(ord(x)), input("Enter string to be converted to array of chars (E.g: Hello, world!): ")))))

hush = xor(list(map(int, input("Enter chars (E.g: 22 83 100 48 105 100 108): ").split(" "))),
           list(map(int, input("Enter key (E.g: 34 12 99): ").split(" "))))


print("Ords:", " ".join(list(map(str, hush))))
print("Chars:", stringify(hush))

