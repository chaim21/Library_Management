def is_empty(txt):
    if len(txt.strip()):
        return txt,None
    return False,"cannot except empty str"