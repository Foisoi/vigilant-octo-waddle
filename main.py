from sys import argv, set_int_max_str_digits

set_int_max_str_digits(100000)

_primes = {2, 3, 5}
_glossary = \
    {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "d",
        16: "f",
        17: "g",
        18: "h",
        19: "i",
        20: "j",
        21: "k",
        22: "l",
        23: "m",
        24: "n",
        25: "o",
        26: "p",
        27: "q",
        28: "r",
        29: "s",
        30: "t",
        31: "u",
        32: "v",
        33: "w",
        34: "x",
        35: "y",
        36: "z",

        37: "-",
        38: "#",
        39: "@",
        40: "*",
        41: "&",

        42: "A",
        43: "B",
        44: "C",
        45: "D",
        46: "E",
        47: "D",
        48: "F",
        49: "G",
        50: "H",
        51: "I",
        52: "J",
        53: "K",
        54: "L",
        55: "M",
        56: "N",
        57: "O",
        58: "P",
        59: "Q",
        60: "R",
        61: "S",
        62: "T",
        63: "U",
        64: "V",
        65: "W",
        66: "X",
        67: "Y",
        68: "Z",
    }


def get_primes(size: int):
    global _primes
    i_ = max(_primes) + 2
    while True:
        c = False
        for prime in _primes:
            if i_ % prime == 0:
                c = True
                break
            c = False
        if not c:
            _primes.add(i_)
        if len(_primes) >= size:
            break
        i_ += 2
    return _primes


def empower(digits: str, _block_size: int):
    _result = 1
    _primes = list(get_primes(min(len(digits), _block_size)))
    for di in range(0, len(digits)):
        digit = int(digits[di]) + di + 2
        power = _primes[di % (len(_primes))]
        _result *= (power ** digit)
    return _result


def mix(number: str, _block_size: int):
    if len(number) % _block_size > 0:
        if len(number) > _block_size:
            number += ((_block_size - (len(number) % _block_size)) * "0")
        else:
            number += ((_block_size - len(number)) * "0")

    mixes = empower(number[0:_block_size], _block_size)
    for bi in range(1, len(number) // _block_size):
        mixed = empower(number[bi * _block_size:(bi + 1) * _block_size], _block_size)
        mixes ^= mixed
    return mixes


def fix(number: str, _block_size: int):
    if len(number) == _block_size:
        return number
    if len(number) % _block_size > 0:
        if len(number) > _block_size:
            number += ((_block_size - (len(number) % _block_size)) * "0")
        else:
            number += ((_block_size - len(number)) * "0")
    final = int(number[0:_block_size])
    for fi in range(1, len(number) // _block_size):
        final ^= int(number[fi * _block_size:(fi + 1) * _block_size])
    return fix(str(final), _block_size)


def stringify(number: str):
    result = ""
    for pi in range(0, len(number) // 2):
        char_code = int(number[pi * 2:(pi + 1) * 2])
        start = 40
        char_code = char_code % (120 - start) + start
        result += chr(char_code)
    return result


def base69(number: str):
    n = int(number)
    result = ""
    while n != 0:
        result += _glossary[n % 69]
        n //= 69
    return result


def charify(string: str) -> str:
    return "".join(map(lambda x: str(ord(x)), string))


if __name__ == "__main__":
    if len(argv) > 2:
        block = 64
        content = " "
        if argv[1] == "-file":
            file = open(argv[2], "r+b")
            content = "".join(list(map(str, file.readlines())))
            file.close()
        elif argv[1] == "-text":
            content = argv[2]
        if len(argv) > 3:
            block = int(argv[3])
        print(base69(fix(str(mix(charify(content), block)), block)))
    else:
        print(f"Wrong arguments. Use:\n main.py -text \"The quick brown fox jumps over a lazy dog\" 43\n main.py -file \"backup_0213.zip\" 70""")
