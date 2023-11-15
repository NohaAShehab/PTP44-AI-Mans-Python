

def formatname(name):
    if isinstance(name, str):
        name=name.strip()
        name=name.capitalize()
        return name

    print("--- error name ")
