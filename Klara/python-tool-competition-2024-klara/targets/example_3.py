def method(x: bool, y: bool) -> int:
    if x:
        s = 1
    else:
        s = 2
    d = 3 if y else 4
    return s + d