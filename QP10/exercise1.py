def square_odds(values:str) -> str:
    ns = values.split(",")
    resul = [int(x)**2 for x in ns if int(x) % 2 != 0]
    return ",".join([str(x) for x in resul])

