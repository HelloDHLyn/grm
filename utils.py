def str_shorten(src: str, length=40) -> str:
    if len(src) <= length:
        return src
    return src[:length] + ' ...'


def str_break_lines(src: str, length=40) -> str:
    results = []
    for line in src.split('\n'):
        results += list(line[i:i+length] for i in range(0, len(line), length))
    return '\n'.join(results)
