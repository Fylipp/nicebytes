_names = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']


def fmt(byte_count):
    if byte_count < 0:
        raise ValueError(f'Value may not be negative: {byte_count}')

    exp, exp_i = _find_exponent(byte_count)

    simple = byte_count / (2 ** exp)
    name = _names[exp_i]
    return f'{simple:.2f} {name} (2**{exp})' if exp_i > 0 else f'{simple:.0f} {name}'


def _find_exponent(n):
    for i in reversed(range(len(_names))):
        pot_exp = 10 * i
        if n >= 2 ** pot_exp:
            return pot_exp, i
    return 0, 0


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('bytes', type=int)
    args = parser.parse_args()

    print(fmt(args.bytes))
