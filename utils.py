def str_shorten(src: str, length=40) -> str:
    if len(src) <= length:
        return src
    return src[:length] + ' ...'
