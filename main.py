from primes import get_primes


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


def charify(string: str) -> str:
    return "".join(map(lambda x: str(ord(x)), string))


block = 64
print("Enter string:")
r = stringify(fix(str(mix(charify(input()), block)), block))
print(r, end="\n")
